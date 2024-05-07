from naoqi import ALProxy
import time

# IP address and port of your NAO robot
nao_ip = "nao.local"
nao_port = 9559

# Create motion proxy
motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)
autonomous_life_proxy = ALProxy("ALAutonomousLife", nao_ip, nao_port)

# Create TTS proxy
tts_proxy = ALProxy("ALTextToSpeech", nao_ip, nao_port)

print("Connected to NAO robot.")

# Text to speech taal voor de robot
language = "Dutch"
tts_proxy.setLanguage(language)
speed = 80
tts_proxy.setParameter("speed", speed)  # Set speech speed

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

# Example usage:
def main():
    # Turn the robot (90 degrees to the right)
    turn_robot(-1.57)  # 1.57 radians is approximately 90 degrees

    # Move arms
    left_arm_angles = [0.5, 0.5, -1.0, 0.5, 0.5, 0.5]
    right_arm_angles = [-0.5, -0.5, 1.0, -0.5, -0.5, -0.5]
    move_arms(left_arm_angles, right_arm_angles)

    # Wait for the robot to finish its movements
    time.sleep(2)  # Adjust as needed

    # Speak slowly
    tts_proxy.say("Hi ik ben NAO. Dit is Ana, Brian, Tyler, Tess en Amin en ons project gaat over mij inzetten zodat ik bingo kan spelen met de ouderen die in het amstelhuis wonen. Ik noem de cijfers op en zij kleuren de cijfers in tot dat ze bingo hebben. Dan ga ik checken of dat ook zo is")
    
    # Reset arms to the rest position
    # move_arms([0] * 6, [0] * 6)

try:
    autonomous_life_proxy.setState("solitary")
    print("Autonomous life started.")
except Exception as e:
    print("Error starting autonomous life:", e)

def wave():
    # Raise right arm
    motion_proxy.setAngles("RShoulderPitch", -0.5, 0.2)  # Angle, speed
    motion_proxy.setAngles("RElbowYaw", 1.0, 0.2)        # Angle, speed
    motion_proxy.setAngles("RElbowRoll", 1.0, 0.2)       # Angle, speed
    
    # Open hand
    motion_proxy.openHand("RHand")

    # Perform waving motion
    for _ in range(2):  # Waving left and right twice
        motion_proxy.setAngles("RElbowYaw", -1.0, 0.2)   # Angle, speed
        time.sleep(0.5)  # Wait for a moment
        motion_proxy.setAngles("RElbowYaw", 1.0, 0.2)    # Angle, speed
        time.sleep(0.5)  # Wait for a moment

    # Reset arm to default position
    motion_proxy.setAngles("RShoulderPitch", 1.0, 0.2)   # Angle, speed
    motion_proxy.setAngles("RElbowYaw", 0.0, 0.2)       # Angle, speed
    motion_proxy.setAngles("RElbowRoll", 0.0, 0.2)      # Angle, speed
    motion_proxy.closeHand("RHand")


# Example usage
if __name__ == "__main__":
    # Example: Make the robot walk forward
    #motion_proxy.walkTo(0.1, 0.1, 0)  # Distance in meters (x, y, theta)

    main()

    #wave()

    #tts_proxy.say("Ja broer ik ga niet voor je liegen mijn niffo is nog in scorro maar ik ben zelf aan het choenen ah zahbi, ik was die challah nog vergeten maar hij balt met die andere m'n kip ouleh")
    
    #tts_proxy.say("Hi ik ben NAO. Dit is Ana, Brian, Tyler, Tess en Amin en ons project gaat over mij inzetten zodat ik bingo kan spelen met de ouderen die in het amstelhuis wonen. Ik noem de cijfers op en zij kleuren de cijfers in tot dat ze bingo hebben. Dan ga ik checken of dat ook zo is")

    time.sleep(5)