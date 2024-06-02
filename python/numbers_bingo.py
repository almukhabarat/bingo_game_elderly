import requests
import threading
from builtins import Exception
from naoqi import ALProxy
import random
import cv2
import numpy as np
import vision_definitions as vd
import time

class BingoSpel:
    def __init__(self, ip="nao.local", port=9559):
        self.ip = ip
        self.port = port
        self.speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)
        self.posture_proxy = ALProxy("ALRobotPosture", ip, port)
        self.motion_proxy = ALProxy("ALMotion", ip, port)
        self.video_service = ALProxy("ALVideoDevice", ip, port)
        self.language = "Dutch"
        self.speed = 100
        self.speech_proxy.setLanguage(self.language)
        self.speech_proxy.setParameter("speed", self.speed)

        self.bingo_bord = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, None]
        ]
        self.opgeroepen_nummers = []
        self.spel_running = False
        self.game_thread = None
        self.qr_thread = None

        # Start polling for commands in a separate thread
        self.poll_thread = threading.Thread(target=self.poll_for_command)
        self.poll_thread.start()

    def start_spel(self):
        # Wake up the robot
        self.motion_proxy.wakeUp()
        # Make the robot stand
        self.posture_proxy.goToPosture("StandInit", 0.5)

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
                response = requests.get('http://145.92.8.134/get_command')
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

    def parse_qr_data(self, data):
        try:
            numbers = [int(data[i:i+2]) for i in range(0, len(data), 2)]
            print("Geparseerde nummers van QR:", numbers)
            if all(nummer in self.opgeroepen_nummers for nummer in numbers):
                self.speech_proxy.say("Bingo! Je hebt alle nummers!")
            else:
                self.speech_proxy.say("Geen bingo. Blijf proberen!")
        except ValueError as e:
            print("Fout bij het parsen van QR code data:", e)
            self.speech_proxy.say("Ongeldige QR code data.")

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
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
