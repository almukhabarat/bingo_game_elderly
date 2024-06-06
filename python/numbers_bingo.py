import requests
import threading
from naoqi import ALProxy
import random
import cv2
import numpy as np
import vision_definitions as vd
import time

class DatabaseHandler:
    def __init__(self, db_url):
        self.db_url = db_url

    def post_request(self, data):
        response = requests.post(self.db_url, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            print('Failed to send data: {response.status_code}')
            return None

class BingoSpel(DatabaseHandler):
    def __init__(self, ip="127.0.0.1", port=59263):
        self.ip = ip
        self.port = port
        self.speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)
        self.posture_proxy = ALProxy("ALRobotPosture", ip, port)
        self.motion_proxy = ALProxy("ALMotion", ip, port)
        self.video_service = ALProxy("ALVideoDevice", ip, port)
        self.db_url = "http://145.92.8.134/bingo_db_post.php"
        self.language = "Dutch"
        self.speed = 100
        self.speech_proxy.setLanguage(self.language)
        self.speech_proxy.setParameter("speed", self.speed)
        self.opgeroepen_nummers = []
        self.spel_running = False
        self.game_thread = None
        self.qr_thread = None
        self.bingo_spel_id = None

        # Start polling for commands in a separate thread
        self.poll_thread = threading.Thread(target=self.poll_for_command)
        self.poll_thread.start()
    
    def new_game_db(self):
        post_game_begin = {
            'query_type': 'post_game_begin',
        }
        response_json = self.post_request(post_game_begin)
        if response_json:
            self.bingo_spel_id = response_json.get('bingoSpelId')
            print('Data sent successfully:', response_json)

    def save_number_to_db(self, number):
        if self.bingo_spel_id is not None:
            post_number = {
                'query_type': 'post_number',
                'bingoSpelId': self.bingo_spel_id,
                'opgenoemd': number
            }
            response_json = self.post_request(post_number)
            if response_json:
                print('Number saved successfully:', response_json)

    def start_spel(self):
        # Wake up the robot
        self.motion_proxy.wakeUp()
        # Make the robot stand
        self.posture_proxy.goToPosture("StandInit", 0.5)

        self.new_game_db()

        self.speech_proxy.say("Welkom bij Bingo!")
        self.spel_running = True
        if self.game_thread is None or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=self.speel_bingo)
            self.game_thread.start()

    def stop_spel(self):
        self.spel_running = False
        if self.game_thread is not None:
            self.game_thread.join()

    def poll_for_command(self):
        while True:
            try:
                response = requests.get('http://145.92.8.134/bingoknop_api/get')
                response.raise_for_status()  # Check if the request was successful
                command = response.json().get('command', None)
                
                if command == 'bingo':
                    print("bingo called")
                    self.stop_spel()
                    self.hoofd_stil(True) # Houdt hoofd stil zodat qr code eenvoudig gescanned kan worden

                    if self.qr_thread is None or not self.qr_thread.is_alive():
                        self.qr_thread = threading.Thread(target=self.start_qr_detection)
                        self.qr_thread.start()
                elif command == 'start':
                    print("game starting")
                    self.start_spel()
                    self.hoofd_stil(False)
            except requests.exceptions.RequestException as e:
                print("HTTP Request failed: ", e)
            time.sleep(1)  # Wait a bit before retrying

    def roep_nummer_op(self):
        while self.spel_running:
            nummer = random.randint(1, 19)
            if nummer not in self.opgeroepen_nummers:
                self.opgeroepen_nummers.append(nummer) # game houdt zelf bij welke nummers zijn omgeroepen
                
                self.save_number_to_db(nummer)

                self.speech_proxy.say("Het volgende nummer is " + str(nummer))
                time.sleep(1)
                self.speech_proxy.say(str(nummer))
                time.sleep(0.5)
                return nummer

    def speel_bingo(self):
        while self.spel_running:
            nummer = self.roep_nummer_op()
            time.sleep(4)
            if self.controleer_winst():
                self.speech_proxy.say("Bingo! We hebben een winnaar!")
                self.stop_spel()
                break

    def controleer_winst(self):
        for row in self.bingo_bord:
            if all(nummer is None or nummer in self.opgeroepen_nummers for nummer in row):
                return True
        return False

    def start_qr_detection(self):
        resolution = vd.kVGA
        color_space = vd.kRGBColorSpace
        fps = 20
        camera_index = 0
        video_client = self.video_service.subscribeCamera("python_client", camera_index, resolution, color_space, fps)
        print("QR detection started")

        try:
            while True:
                nao_image = self.video_service.getImageRemote(video_client)
                if nao_image is None:
                    print("Kon geen afbeelding van de camera krijgen.")
                    continue

                image_width = nao_image[0]
                image_height = nao_image[1]
                array = nao_image[6]
                image = np.frombuffer(array, dtype=np.uint8).reshape((image_height, image_width, 3))
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                qr_detector = cv2.QRCodeDetector()
                data, bbox, _ = qr_detector.detectAndDecode(image)

                if bbox is not None and data:
                    print("QR Code Gedetecteerd!!")
                    print(data)
                    self.speech_proxy.say("QR code gedetecteerd.")
                    self.parse_qr_data(data)
                    break

                time.sleep(1)
        finally:
            self.video_service.unsubscribe(video_client)
            cv2.destroyAllWindows()

    # Deze functie kan later nog in een aparte movement class komen
    def hoofd_stil(self, freeze):
        # Positioneerd hoofdpositie naar voren
        if freeze:
            head_joints = ["HeadYaw", "HeadPitch"]
            angles = [0.0, 0.0]  # 0.0, hoofd is gecentreerd
            fractionMaxSpeed = 0.1
            self.motion_proxy.setAngles(head_joints, angles, fractionMaxSpeed)

            # Stijfheid van het hoofd
            stiffness = 1.0 if freeze else 0.0
            self.motion_proxy.setStiffnesses(head_joints, stiffness)

def main():
    bingo_spel = BingoSpel()

if __name__ == "__main__":
    main()