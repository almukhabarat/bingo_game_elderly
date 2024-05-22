import requests

def check_stepper_activation():
    # Replace 'http://yourflaskserver.com/trigger' with the actual URL of your Flask API
    response = requests.get('http://192.92.8.134/trigger')
    if response.status_code == 200 and response.text.strip() == 'Stepper motor activated':
        return True
    else:
        return False

if __name__ == '__main__':
    if check_stepper_activation():
        print("Stepper motor should be activated")
        # Add your logic here to perform any necessary actions when the stepper motor should be activated
    else:
        print("Stepper motor should not be activated")
