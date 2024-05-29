# Import necessary modules
import sys
from naoqi import ALProxy

# Define NAO's IP address and port
NAO_IP = "nao.local"  # Replace with your NAO's IP address
NAO_PORT = 9559

# Connect to the necessary NAOqi modules
try:
    face_detection_proxy = ALProxy("ALFaceDetection", NAO_IP, NAO_PORT)
except Exception as e:
    print("Error when creating proxy:", e)
    sys.exit(1)

# Subscribe to the face detection event
face_detection_proxy.subscribe("FaceDetection", 500, 0.0)

try:
    while True:
        # Retrieve face detection results
        face_info = face_detection_proxy.getFaceDetectionResults()

        # Check if face(s) detected
        if face_info and isinstance(face_info, list):
            # Print face information
            for face in face_info:
                print("Face detected at position:", face[0])
        else:
            print("No face detected")

except KeyboardInterrupt:
    print("Interrupted by user, stopping face detection...")

# Unsubscribe from the face detection event
face_detection_proxy.unsubscribe("FaceDetection")
