from naoqi import ALProxy
import time
import cv2
import numpy as np
from PIL import Image
import zbarlight

nao_ip = "nao.local"  # NAO's IP address or simulation
nao_port = 9559  # Default port for NAO

# Proxies
motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)
tts_proxy = ALProxy("ALTextToSpeech", nao_ip, nao_port)
autonomous_life_proxy = ALProxy("ALAutonomousLife", nao_ip, nao_port)
camera_proxy = ALProxy("ALVideoDevice", nao_ip, nao_port)
print("Connected to NAO robot.")

# Text to speech language for the robot
language = "Dutch"
tts_proxy.setLanguage(language)

# Start autonomous life
try:
    autonomous_life_proxy.setState("solitary")
    print("Autonomous life started.")
except Exception as e:
    print("Error starting autonomous life:", e)

def capture_image():
    # Select the top camera, resolution and color space
    camera_proxy.setParam(18, 0)  # Camera selection: 0-top, 1-bottom
    resolution = 2  # VGA
    colorSpace = 11  # RGB

    video_client = camera_proxy.subscribe("python_client", resolution, colorSpace, 5)
    nao_image = camera_proxy.getImageRemote(video_client)
    camera_proxy.unsubscribe(video_client)

    # Get the image size and data
    image_width = nao_image[0]
    image_height = nao_image[1]
    array = np.frombuffer(nao_image[6], dtype=np.uint8).reshape((image_height, image_width, 3))

    # Convert to grayscale
    gray_image = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    return gray_image

def decode_qr_code(image):
    # Decode QR code
    codes = zbarlight.scan_codes('qrcode', Image.fromarray(image))
    return codes

# Example usage
# if __name__ == "__main__":
#     image = capture_image()
#     qr_code_contents = decode_qr_code(image)
# 
#     if qr_code_contents:
#         print("QR Code detected:", qr_code_contents[0])
#         tts_proxy.say("QR code content is: " + qr_code_contents[0])
#     else:
#         print("No QR code detected.")
#         tts_proxy.say("No QR code detected.")

#     time.sleep(5)