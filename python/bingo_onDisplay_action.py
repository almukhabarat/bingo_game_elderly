from naoqi import ALProxy
import time

class NaoInit:
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self._language = "dutch"
        self._tts_speed = 100
        self._motion_proxy = ALProxy("ALMotion", self._ip, self._port)
        self._posture_proxy = ALProxy("ALRobotPosture", self._ip, self._port)
        self._tts_proxy = ALProxy("ALTextToSpeech", self._ip, self._port)

    def wake_up(self):
        self._motion_proxy.wakeUp()

    def rest(self):
        self._motion_proxy.rest()
    
    def speech(self, text):
        self._tts_proxy.setLanguage(self._language)
        self._tts_proxy.setParameter("speed", self._tts_speed)
        self._tts_proxy(text)
        
class Movement(NaoInit):
    def dance(self):
        self._posture_proxy.goToPosture("StandInit", 0.5)
        names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", 
                 "RShoulderPitch", "RShoulderRoll", "HipRoll", "HipPitch"]
        angles = [[0.5, -0.5], [0.3, -0.3], [1.0, 0.5], [0.5, -0.5], 
                  [1.0, 0.5], [-0.5, 0.5], [0.3, -0.3], [0.3, -0.3]]
        times = [[1.0, 2.0], [1.0, 2.0], [1.0, 2.0], [1.0, 2.0], 
                 [1.0, 2.0], [1.0, 2.0], [1.0, 2.0], [1.0, 2.0]]
        for name, angle, time in zip(names, angles, times):
            self._motion_proxy.angleInterpolation(name, angle, time, True)
        # self.speech("I love dancing!")
    
    def wave(self):
        # Rechter arm omhoog met hand open
        name = ["RShoulderPitch", "RElbowYaw", "RElbowRoll"]
        angle = [-0.5, 1.0, 1,0]
        speed = [0.2, 0.2, 0.2]

        for names, angles, speeds in zip(name, angle, speed):
            self._motion_proxy.setAngles(names, angles, speeds)

        self._motion_proxy.openHand("RHand")

        # Zwaaibeweging (loopt 2x)
        # for _ in range(2):  # Waving left and right twice
        #     self._motion_proxy.setAngles("RElbowYaw", -1.0, 0.2)   # Angle, speed
        #     time.sleep(0.5)  # Wait for a moment
        #     self._motion_proxy.setAngles("RElbowYaw", 1.0, 0.2)    # Angle, speed
        #     time.sleep(0.5)  # Wait for a moment

        # ARM BEWEGINGEN

        # Define the joints, angles, and speeds for the handwave
        joint = "RWristYaw"
        wave_angles = [0.5, -0.5]  # Angles for the wave motion
        speed = 0.2  # Speed of the movement
        wave_count = 2  # Number of waves
        delay_between_waves = 0.5  # Time delay between waves

        # Perform the waving motion
        for _ in range(wave_count):
            for angle in wave_angles:
                self._motion_proxy.setAngles(joint, angle, speed)
                time.sleep(delay_between_waves)
                
        # Optionally, return the wrist to a neutral position
        self._motion_proxy.setAngles(joint, 0.0, speed)
                
        self._motion_proxy.closeHand("RHand")

        

if __name__ == "__main__":
    ip = "127.0.0.1"  # Replace with your NAO robot's IP address
    port = 52852
    move = Movement(ip, port)

    move.wake_up()
    move.wave()
    # move.rest()

    # waving_nao.wake_up()
    # waving_nao.wave()
    # waving_nao.rest()

#####################################################

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