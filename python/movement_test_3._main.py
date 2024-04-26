from naoqi import ALProxy
import time

nao_ip = "nao.local"  # Replace with your NAO's IP address
nao_port = 9559  # Default port for NAO

motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)
tts_proxy = ALProxy("ALTextToSpeech", nao_ip, nao_port)
autonomous_life_proxy = ALProxy("ALAutonomousLife", nao_ip, nao_port)
print("Connected to NAO robot.")

# Text to speech taal voor de robot
language = "Dutch"
tts_proxy.setLanguage(language)

#slower_rate = 0.5
#tts_proxy.setParameter("speed", slower_rate)

# Start autonomous life
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

    wave()

    tts_proxy.say("Ja broer ik ga niet voor je liegen mijn niffo is nog in scorro maar ik ben zelf aan het choenen ah zahbi, ik was die challah nog vergeten maar hij balt met die andere m'n kip ouleh")
    
    #tts_proxy.say("Hi ik ben NAO. Dit is Ana, Brian, Tyler, Tess en Amin en ons project gaat over mij inzetten zodat ik bingo kan spelen met de ouderen die in het amstelhuis wonen. Ik noem de cijfers op en zij kleuren de cijfers in tot dat ze bingo hebben. Dan ga ik checken of dat ook zo is")

    time.sleep(5)