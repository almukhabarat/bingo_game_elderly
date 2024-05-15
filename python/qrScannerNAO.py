# Revised NAO robot script for continuous QR code detection using OpenCV

from naoqi import ALProxy
import cv2
import numpy as np
import vision_definitions as vd
import time

nao_ip = "nao.local"  # Replace with your NAO's IP address
nao_port = 9559  # Default port for NAO

# Setting up proxies
video_service = ALProxy("ALVideoDevice", nao_ip, nao_port)
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
autonomous_life = ALProxy("ALAutonomousLife", nao_ip, nao_port)

# Set the language for TTS
tts.setLanguage("English")

# Subscribe to the top camera
resolution = vd.kVGA  # 640 x 480
color_space = vd.kRGBColorSpace
fps = 20
camera_index = 0  # 0 for top camera, 1 for bottom camera
video_client = video_service.subscribeCamera("python_client", camera_index, resolution, color_space, fps)

def continuous_qr_detection():
    try:
        while True:
            # Get a frame from the camera
            nao_image = video_service.getImageRemote(video_client)
            if nao_image is None:
                print("Failed to get image from camera.")
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
                print("QR Code Detected!!")
                print(data)
                tts.say(data)  # NAO speaks the QR code data
            
            time.sleep(1)  # Delay to allow for TTS to finish and prevent rapid re-reading of the same QR code
            
    finally:
        video_service.unsubscribe(video_client)
        cv2.destroyAllWindows()

# If this script is run directly, start the detection
if __name__ == "__main__":
    autonomous_life.setState("disabled")  # Disable autonomous life to keep the head still
    continuous_qr_detection()