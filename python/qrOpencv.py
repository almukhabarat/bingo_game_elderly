import cv2

def read_qrcodes_opencv():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    qr_detector = cv2.QRCodeDetector()

    if not cap.isOpened():
        print("Error: Camera could not be accessed.")
        return

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Frame could not be read.")
                break

            # Detect and decode QR code
            data, bbox, _ = qr_detector.detectAndDecode(frame)

            # Check if there is a QR code in the image
            if bbox is not None and data:
                print("QR Code Detected:")
                print("Data:", data)

            # Display the resulting frame (optional, can be removed for terminal-only usage)
            cv2.imshow('QR Code Reader', frame)

            # Exit loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    read_qrcodes_opencv()