from naoqi import ALProxy
import time

# IP address and port of your NAO robot
ip = "nao.local"
port = 9559

# Create motion proxy
motion_proxy = ALProxy("ALMotion", ip, port)

# Create TTS proxy
tts_proxy = ALProxy("ALTextToSpeech", ip, port)

def turn_robot(angle):
    """
    Turn the robot by the specified angle in radians.
    """
    motion_proxy.moveTo(0, 0, angle)

def move_arms(left_angles, right_angles):
    """
    Move the robot's arms to the specified joint angles.
    """
    motion_proxy.setAngles("LArm", left_angles, 0.5)
    motion_proxy.setAngles("RArm", right_angles, 0.5)

def say_text(text):
    """
    Make the robot speak the specified text.
    """
    tts_proxy.say(text)

# Example usage:
def main():
    # Turn the robot (90 degrees to the right)
    turn_robot(1.57)  # 1.57 radians is approximately 90 degrees

    # Move arms
    left_arm_angles = [0.5, 0.5, -1.0, 0.5, 0.5, 0.5]
    right_arm_angles = [-0.5, -0.5, 1.0, -0.5, -0.5, -0.5]
    move_arms(left_arm_angles, right_arm_angles)

    # Wait for the robot to finish its movements
    time.sleep(2)  # Adjust as needed

    # Speak
    say_text("Ik doe al 25 jaar geen belasting aangifte")
    
    # Reset arms to the rest position
    move_arms([0] * 6, [0] * 6)


if __name__ == "__main__":
    main()
