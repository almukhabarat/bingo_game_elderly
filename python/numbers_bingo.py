from naoqi import ALProxy
import random

class BingoSpel:
    def __init__(self, ip="nao.local", port=9559):
        self.ip = ip
        self.port = port
        #   NAOqi proxies (ingebouwde events)
        self.speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)
        # de nummers van het bingobord
        self.bingo_bord = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

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

    def roep_nummer_op(self, opgeroepen_nummers):
        while True:
            # kiest een willekeurig nummer
            nummer = random.randint(1, 25)
            if nummer not in opgeroepen_nummers:
                opgeroepen_nummers.append(nummer)
                # Aankondigen van het nummer
                self.speech_proxy.say("Het volgende nummer is " + str(nummer))
                return nummer

    def speel_bingo(self):
        opgeroepen_nummers = [] 
        while True:
            nummer = self.roep_nummer_op(opgeroepen_nummers)
            # Controleren op winnende patroon
            if self.controleer_winst(self.bingo_bord, opgeroepen_nummers):
                # Aankondigen van de winnaar
                self.speech_proxy.say("Bingo! We hebben een winnaar!")
                break

    def controleer_winst(self, bord, opgeroepen_nummers):
        # placeholder  om later de qr code te kunnen zetten 
        return False  

if __name__ == "__main__":
    # melden van BingoSpel en starten van het spel
    bingo_spel = BingoSpel()
    bingo_spel.start_spel()
