# Documentatie voor BingoSpel Python-code

Deze documentatie biedt een overzicht en uitleg van de Python-code voor de klasse BingoSpel, die een bingospel mogelijk maakt met behulp van de NAO-robot en een database.

## Class: BingoSpel

### Initialization (__init__ method)

```python
class BingoSpel:
    def __init__(self, ip="localhost", port=65355):
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
        self.bingo_spel_id = None

        # Start polling for commands in a separate thread
        self.poll_thread = threading.Thread(target=self.poll_for_command)
        self.poll_thread.start()
```

In de `__init__` method worden verschillende proxy's geïnitieerd om verbinding te maken met de modules van de NAO-robot zoals tekst-naar-spraak, autonoom leven, robot houding, beweging en videodienst. De URL voor interactie met de database van het bingospel wordt ingesteld. Daarnaast worden de taal en snelheid voor spraak ingesteld. Het bingobord, de lijst van opgeroepen nummers, spelstatus, en threads voor het spel en QR-detectie worden geïnitialiseerd. Tot slot wordt een aparte thread gestart om te polleren voor commando's.

### new_game_db Method

```python
def new_game_db(self):
    post_game_begin = {'query_type': 'post_game_begin'}
    new_game_db = requests.post(self.db_url, data=post_game_begin)
    if new_game_db.status_code == 200:
        print('Data sent successfully:', new_game_db.text)
        self.bingo_spel_id = new_game_db.json().get('bingoSpelId')
    else:
        print('Failed to send data:', new_game_db.status_code, new_game_db.text)
```

De `new_game_db` method stuurt een verzoek naar de database om een nieuw spel te starten en haalt het spel-ID op. Bij een succesvolle HTTP-respons wordt een succesbericht afgedrukt; anders wordt een foutmelding weergegeven.

### save_number_to_db Method

```python
def save_number_to_db(self, number):
    if self.bingo_spel_id is not None:
        post_number = {
            'query_type': 'post_number',
            'bingoSpelId': self.bingo_spel_id,
            'opgenoemd': number
        }
        response = requests.post(self.db_url, data=post_number)
        if response.status_code == 200:
            print('Number saved successfully:', response.text)
        else:
            print('Failed to save number:', response.status_code, response.text)
```

De `save_number_to_db` method slaat het opgeroepen bingonummer op in de database. Bij een succesvolle HTTP-respons wordt een succesbericht afgedrukt; anders wordt een foutmelding weergegeven.

### start_spel Method

```python
def start_spel(self):
    self.motion_proxy.wakeUp()
    self.posture_proxy.goToPosture("StandInit", 0.5)
    self.new_game_db()
    self.speech_proxy.say("Welkom bij Bingo!")
    self.spel_running = True
    if self.game_thread is None or not self.game_thread.is_alive():
        self.game_thread = threading.Thread(target=self.speel_bingo)
        self.game_thread.start()
```

De `start_spel` method start het bingospel door de robot wakker te maken, de houding in te stellen, een nieuw spel in de database te initialiseren en de spelthread te starten. De robot kondigt vervolgens de start van het spel aan.

### stop_spel Method

```python
def stop_spel(self):
    self.spel_running = False
    if self.game_thread is not None:
        self.game_thread.join()
```

De `stop_spel` method stopt het bingospel en zorgt ervoor dat de spelthread is voltooid.

### poll_for_command Method

```python
def poll_for_command(self):
    while True:
        try:
            response = requests.get('http://145.92.8.134/api/get_command')
            response.raise_for_status()
            command = response.json().get('command', None)
            
            if command == 'bingo':
                print("bingo called")
                self.stop_spel()
                self.hoofd_stil(True)
                if self.qr_thread is None or not self.qr_thread.is_alive():
                    self.qr_thread = threading.Thread(target=self.start_qr_detection)
                    self.qr_thread.start()
            elif command == 'start':
                print("game starting")
                self.start_spel()
                self.hoofd_stil(False)
        except requests.exceptions.RequestException as e:
            print("HTTP Request failed: ", e)
        time.sleep(1)
```

De `poll_for_command` method pollt continu voor commands van een gespecificeerde API-endpoint. Het behandelt de commands "bingo" en "start" door respectievelijk het spel te stoppen of te starten en de hoofdpositie van de robot aan te passen voor QR-code detectie.

### roep_nummer_op Method

```python
def roep_nummer_op(self):
    while self.spel_running:
        nummer = random.randint(1, 19)
        if nummer not in self.opgeroepen_nummers:
            self.opgeroepen_nummers.append(nummer)
            self.save_number_to_db(nummer)
            self.speech_proxy.say("Het volgende nummer is " + str(nummer))
            time.sleep(1)
            self.speech_proxy.say(str(nummer))
            time.sleep(0.5)
            return nummer
```

De `roep_nummer_op` method roept een willekeurig bingonummer en kondigt het aan via de spraakproxy van de robot, waarna het nummer in de database wordt opgeslagen. De methode zorgt ervoor dat het nummer nog niet eerder is opgeroepen.

### speel_bingo Method

```python
def speel_bingo(self):
    while self.spel_running:
        nummer = self.roep_nummer_op()
        time.sleep(4)
        if self.controleer_winst():
            self.speech_proxy.say("Bingo! We hebben een winnaar!")
            self.stop_spel()
            break
```

De `speel_bingo` methode roept continu bingonummers op en controleert of er een winnende rij op het bingobord is. Bij een winconditie kondigt de robot de winst aan en stopt het spel.

### start_qr_detection Method

```python
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

            if bbox is not None en data:
                print("QR Code Gedetecteerd!!")
                print(data)
                self.speech_proxy.say("QR code gedetecteerd.")
                self.parse_qr_data(data)
                break

            time.sleep(1)
    finally:
        self.video_service.unsubscribe(video_client)
        cv2.destroyAllWindows()
```

De `start_qr_detection` method detecteert QR-codes met behulp van de camera van de robot en OpenCV. De loop maakt continu afbeeldingen van de camera, verwerkt deze en controleert op QR-codes.

## Main function

```python
def main():
    bingo_spel = BingoSpel()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
```

De hoofdfunctie initialiseert de `BingoSpel` Class en houdt het programma draaiende totdat het wordt onderbroken. Bij een onderbreking door de gebruiker wordt een afsluitbericht afgedrukt.