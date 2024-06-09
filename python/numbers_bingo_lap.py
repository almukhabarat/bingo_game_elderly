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
        try:
            response = requests.post(self.db_url, data=data)
            response.raise_for_status()  # Raises an error for bad status codes
            try:
                return response.json()
            except ValueError:
                print('Response is not in JSON format: {}'.format(response.text))
                return None
        except requests.exceptions.RequestException as e:
            print('Failed to send data: {}'.format(e))
            return None

class BingoSpel(DatabaseHandler):
    def __init__(self, ip="127.0.0.1", port=58600):
        DatabaseHandler.__init__(self, "http://145.92.8.134/bingo_db_post.php")
        self.ip = ip
        self.port = port
        self.speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)
        self.posture_proxy = ALProxy("ALRobotPosture", ip, port)
        self.motion_proxy = ALProxy("ALMotion", ip, port)
        self.language = "Dutch"
        self.speed = 100
        self.speech_proxy.setLanguage(self.language)
        self.speech_proxy.setParameter("speed", self.speed)
        self.opgeroepen_nummers = []
        self.spel_running = False
        self.game_thread = None
        self.qr_thread = None
        self.bingo_spel_id = None
        self.qr_code_numbers = []  # To store numbers from the bingo card
        self.ball_ready_event = threading.Event()  # Event to signal when the ball is ready

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
            print('Data sent successfully: {}'.format(response_json))

    def save_number_to_db(self, number):
        if self.bingo_spel_id is not None:
            post_number = {
                'query_type': 'post_number',
                'bingoSpelId': self.bingo_spel_id,
                'opgenoemd': number
            }
            response_json = self.post_request(post_number)
            if response_json:
                print('Number saved successfully: {}'.format(response_json))

    def fetch_bingo_card(self, bingo_kaart_id):
        post_data = {
            'query_type': 'get_bingo_card',
            'bingoKaartId': bingo_kaart_id
        }
        response_json = self.post_request(post_data)
        if response_json:
            if 'error' in response_json:
                print('Error fetching bingo card: {}'.format(response_json['error']))
            else:
                card_numbers = response_json.get('getal')
                if card_numbers:
                    self.qr_code_numbers = list(map(int, card_numbers.split(',')))
                    print('Fetched Bingo Card Numbers: {}'.format(self.qr_code_numbers))
                else:
                    print('Failed to fetch bingo card numbers.') 
        else:
            print('Failed to fetch bingo card.')

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

    def resume_spel(self):
        self.spel_running = True
        if self.game_thread is None or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=self.speel_bingo)
            self.game_thread.start()

    def poll_for_command(self):
        while True:
            try:
                # Poll for the "bingo" or "start" command
                response = requests.get('http://145.92.8.134/bingoknop_api/get')
                response.raise_for_status()  # Check if the request was successful
                command = response.json().get('command', None)
                
                if command == 'bingo':
                    print("bingo called")
                    self.stop_spel()
                    self.hoofd_stil(True)  # Houdt hoofd stil zodat qr code eenvoudig gescanned kan worden

                    if self.qr_thread is None or not self.qr_thread.is_alive():
                        self.qr_thread = threading.Thread(target=self.start_qr_detection)
                        self.qr_thread.start()

                elif command == 'start':
                    print("game starting")
                    self.start_spel()
                    self.hoofd_stil(False)

            except requests.exceptions.RequestException as e:
                print("HTTP Request failed (bingoknop_api): {}".format(e))

            try:
                # Poll for the "bal op positie" command
                response = requests.get('http://145.92.8.134/bingobal_api/get')
                response.raise_for_status()  # Check if the request was successful
                command = response.json().get('command', None)
                
                if command == 'bal op positie':
                    print("Command received: bal op positie")
                    self.ball_ready_event.set()  # Signal that the ball is ready

            except requests.exceptions.RequestException as e:
                print("HTTP Request failed (bingobal_api): {}".format(e))
            
            time.sleep(1)  # Wait a bit before retrying

    def roep_nummer_op(self):
        while self.spel_running:
            nummer = random.randint(1, 19)
            if nummer not in self.opgeroepen_nummers:
                self.opgeroepen_nummers.append(nummer)  # game houdt zelf bij welke nummers zijn omgeroepen
                
                self.save_number_to_db(nummer)

                self.draai_molen()
                self.speech_proxy.say("Het volgende nummer is {}".format(nummer))
                time.sleep(1)
                self.speech_proxy.say(str(nummer))
                time.sleep(0.5)
                return nummer
            
    def draai_molen(self):
        data = {"command": "Draaien pls"}
        try:
            print("Sending POST request to start the wheel turning...")
            response = requests.post('http://145.92.8.134/bingobal_api/post', json=data)
            response.raise_for_status()
            print("POST request sent successfully: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            print('Failed to send POST request: {}'.format(e))
            return
        
        print("Waiting for ball to be ready...")
        self.ball_ready_event.wait()  # Wait for the event to be set
        print("Ball is ready!")
        self.ball_ready_event.clear()  # Clear the event for the next round

    def speel_bingo(self):
        while self.spel_running:
            nummer = self.roep_nummer_op()
            time.sleep(4)

    def controleer_winst(self):
        # 3x3 grid win conditions
        win_conditions = [
            # Rows
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8],
            # Columns
            [0, 3, 6], 
            [1, 4, 7], 
            [2, 5, 8],
            # Diagonals
            [0, 4, 8], 
            [2, 4, 6]
        ]
        
        print("Checking win conditions")
        print("Called numbers: {}".format(self.opgeroepen_nummers))
        print("QR code numbers: {}".format(self.qr_code_numbers))

        if len(self.qr_code_numbers) != 9:
            print("Invalid bingo card size.")
            return False
        
        for condition in win_conditions:
            condition_numbers = [self.qr_code_numbers[i] for i in condition]
            print("Checking condition: {} -> {}".format(condition, condition_numbers))
            
            if all(number in self.opgeroepen_nummers for number in condition_numbers):
                print("Winning condition met: {}".format(condition))
                return True

        print("No winning condition met.")
        self.resume_spel()
        return False
    
    def start_qr_detection(self):

        # Initialize the video service
        self.video_service = ALProxy("ALVideoDevice", self.ip, self.port)
    
        resolution = vd.kVGA
        color_space = vd.kRGBColorSpace
        fps = 20
        camera_index = 0
        video_client = self.video_service.subscribeCamera("python_client", camera_index, resolution, color_space, fps)
        print("QR detection started")

        qr_detector = cv2.QRCodeDetector()

        try:
            while True:
                nao_image = self.video_service.getImageRemote(video_client)
                if nao_image is None:
                    print("Kon geen afbeelding van de camera krijgen.")

                image_width = nao_image[0]
                image_height = nao_image[1]
                array = nao_image[6]
                image = np.frombuffer(array, dtype=np.uint8).reshape((image_height, image_width, 3))
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                data, bbox, _ = qr_detector.detectAndDecode(image)

                if bbox is not None and data:
                    print("QR Code Detected:")
                    print(data)
                    self.fetch_bingo_card(int(data))  # Fetch the bingo card numbers using the bingoKaartId

                    # Check for win after scanning the QR code
                    if self.controleer_winst():
                        self.speech_proxy.say("Bingo! We hebben een winnaar!")
                    else:
                        self.speech_proxy.say("Geen Bingo! Probeer opnieuw.")
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