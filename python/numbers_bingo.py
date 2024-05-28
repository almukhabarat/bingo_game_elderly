from naoqi import ALProxy
import random
import cv2
import numpy as np
import vision_definitions as vd
import time
import threading

class BingoSpel:
    def __init__(self, ip="nao.local", port=9559):
        self.ip = ip
        self.port = port
        #   NAOqi proxies (ingebouwde events)
        self.speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)
        self.video_service = ALProxy("ALVideoDevice", ip, port)
        # Stel taal en snelheid in voor de robot
        self.language = "Dutch"
        self.speed = 100
        self.speech_proxy.setLanguage(self.language)
        self.speech_proxy.setParameter("speed", self.speed)
        # de nummers van het bingobord
        self.bingo_bord = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, None]
        ]
        self.opgeroepen_nummers = []

    def start_spel(self):
        try:
            # Starten van de autonomous life 
            self.autonomous_life_proxy.setState("solitary")
            print("Autonomous life started")
        except Exception as e:
            print("Fout bij het starten van autonomous life:", e)

        # Begroeting van spelers
        self.speech_proxy.say("Welkom bij Bingo!")

        # Starten van het Bingo spel
        self.speel_bingo()

    def roep_nummer_op(self):
        while True:
            # kiest een willekeurig nummer tussen 1 en 19
            nummer = random.randint(1, 19)
            if nummer not in self.opgeroepen_nummers:
                self.opgeroepen_nummers.append(nummer)
                # Aankondigen van het nummer
                self.speech_proxy.say("Het volgende nummer is " + str(nummer))
                time.sleep(1)
                # Herhaal het nummer
                self.speech_proxy.say(str(nummer))
                time.sleep(0.5)
                return nummer
    def speel_bingo(self):
        while True:
            nummer = self.roep_nummer_op()
            time.sleep(4)
            if self.controleer_winst():
                self.speech_proxy.say("Bingo! We hebben een winnaar!")
                break

    def controleer_winst(self):
        # Controleer of alle nummers op het bingobord in de opgeroepen nummers lijst staan
        for row in self.bingo_bord:
            if all(nummer is None or nummer in self.opgeroepen_nummers for nummer in row):
                return True
        return False

    def start_qr_detection(self):
        # Instellen van de camera-instellingen
        resolution = vd.kVGA
        color_space = vd.kRGBColorSpace
        fps = 20
        camera_index = 0
        video_client = self.video_service.subscribeCamera("python_client", camera_index, resolution, color_space, fps)

        try:
            while True:
                # Een frame van de camera ophalen
                nao_image = self.video_service.getImageRemote(video_client)
                if nao_image is None:
                    print("Kon geen afbeelding van de camera krijgen.")
                    continue
                
                # Extract image data
                image_width = nao_image[0]
                image_height = nao_image[1]
                array = nao_image[6]
                image = np.frombuffer(array, dtype=np.uint8).reshape((image_height, image_width, 3))
                
                # Convert to BGR format for OpenCV
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                # Detect and decode QR code using OpenCV
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
            # Parse de QR code data naar een lijst van nummers
            numbers = [int(data[i:i+2]) for i in range(0, len(data), 2)]
            print("Geparseerde nummers van QR:", numbers)
            if all(nummer in self.opgeroepen_nummers for nummer in numbers):
                self.speech_proxy.say("Bingo! Je hebt alle nummers!")
            else:
                self.speech_proxy.say("Geen bingo. Blijf proberen!")
        except ValueError as e:
            print("Fout bij het parsen van QR code data:", e)
            self.speech_proxy.say("Ongeldige QR code data.")

def main():
    bingo_spel = BingoSpel()
    
    # Start het Bingo spel in een aparte thread
    threading.Thread(target=bingo_spel.start_spel).start()
    

if __name__ == "__main__":
    main()