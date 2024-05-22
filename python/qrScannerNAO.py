from naoqi import ALProxy
import cv2
import numpy as np
import vision_definitions as vd
import time

nao_ip = "nao.local"  # Vervang dit door het IP-adres van uw NAO
nao_port = 9559  # Standaardpoort voor NAO

# Het instellen van proxies
video_service = ALProxy("ALVideoDevice", nao_ip, nao_port)
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
autonomous_life = ALProxy("ALAutonomousLife", nao_ip, nao_port)

# Stel de taal in voor TTS (Text-to-Speech)
tts.setLanguage("English")

# Abonneren op de bovenste camera
resolution = vd.kVGA  # 640 x 480
color_space = vd.kRGBColorSpace
fps = 20
camera_index = 0  # 0 voor de bovenste camera, 1 voor de onderste camera
video_client = video_service.subscribeCamera("python_client", camera_index, resolution, color_space, fps)

def continuous_qr_detection():
    try:
        while True:
            # Verkrijg een frame van de camera
            nao_image = video_service.getImageRemote(video_client)
            if nao_image is None:
                print("Mislukt om afbeelding van de camera te verkrijgen.")
                continue
            
            # Haal beeldgegevens op
            image_width = nao_image[0]
            image_height = nao_image[1]
            array = nao_image[6]
            image = np.frombuffer(array, dtype=np.uint8).reshape((image_height, image_width, 3))
            
            # Converteer naar BGR-formaat voor OpenCV
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Detecteer en decodeer QR-code met OpenCV
            qr_detector = cv2.QRCodeDetector()
            data, bbox, _ = qr_detector.detectAndDecode(image)

            if bbox is not None and data:
                print("QR Code Gedetecteerd!!")
                print(data)
                tts.say(data)  # NAO spreekt de QR-code gegevens uit
            
            time.sleep(1)  # Vertraging om TTS te laten voltooien en snelle herlezing van dezelfde QR-code te voorkomen
            
    finally:
        video_service.unsubscribe(video_client)
        cv2.destroyAllWindows()

# Als dit script direct wordt uitgevoerd, start de detectie
if __name__ == "__main__":
    autonomous_life.setState("disabled")  # Schakel autonoom leven uit om het hoofd stil te houden
    continuous_qr_detection()