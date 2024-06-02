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

        self.url = "145.92.8.134/bingo_db.php"

        # Start polling for commands in a separate thread
        self.poll_thread = threading.Thread(target=self.poll_for_command)
        self.poll_thread.start()

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
                
                post_getal = requests.post(self.url, data=) 

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


def main():
    bingo_spel = BingoSpel()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
