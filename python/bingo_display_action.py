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
    def wave(self):
        # Alle namen die gebruikt worden voor het aansturen van de rechter arm 
        wave_names = ["RShoulderPitch", "RElbowYaw", "RElbowRoll", "RWristYaw", "RShoulderRoll"]

        # Rechter arm omhoog met hand open
        arm_names = [wave_names[0], wave_names[1], wave_names[2]]
        angle_up = [-0.5, 1.0, 1,0]
        up_speeds = [0.2, 0.2, 0.2]

        for name, angle, speed in zip(arm_names, angle_up, up_speeds):
            self._motion_proxy.setAngles(name, angle, speed)

        self._motion_proxy.openHand("RHand")

        # Zwaai beweging door middel van elleboog en pols rotaties
        wrist_angles = [0.3, -0.7] # Zwaaien van de hand
        elbow_angles = [-1.0, 1.0] # Zwaaien van de elleboog
        shoulder_angles = [0.0, -0.3] # Zwaaien van de schouder
        wave_times = 2
        delay_between_waves = 0.5

        for _ in range(wave_times):
            for wrist_angle, elbow_angle, shoulder_angle in zip(wrist_angles, elbow_angles, shoulder_angles):
                self._motion_proxy.setAngles(wave_names[3], wrist_angle, 0.3) # "RWristYaw", hoek, animatiesnelheid
                self._motion_proxy.setAngles(wave_names[1], elbow_angle, 0.2) # "RElbowYaw", hoek, animatiesnelheid
                self._motion_proxy.setAngles(wave_names[4], shoulder_angle, 0.2) # "RShoulderRoll", hoek, animatiesnelheid
                time.sleep(delay_between_waves)
        
        # Neutrale positionering van de rechter arm
        reset_angles = [1.0, 0.0, 0.0, 0.0, 0.0]

        for name, angle in zip(wave_names, reset_angles):
            self._motion_proxy.setAngles(name, angle, 0.2)
                
        self._motion_proxy.closeHand("RHand")
        
        head_joints = ["HeadYaw", "HeadPitch"]
        self._motion_proxy.setStiffnesses(head_joints, 0.0)

    def freezeHead(self):
        # Optionally, set the head to a specific position
        # For example, head centered:
        names = ["HeadYaw", "HeadPitch"]
        angles = [0.0, 0.0]  # 0.0 radians means the head is centered
        fractionMaxSpeed = 0.1
        self._motion_proxy.setAngles(names, angles, fractionMaxSpeed)

        # Set stiffness of the head joints to keep it in place
        head_joints = ["HeadYaw", "HeadPitch"]
        stiffness = 1.0
        self._motion_proxy.setStiffnesses(head_joints, stiffness)

        

if __name__ == "__main__":
    # ip = "nao.local"  # NAO robot via ethernet
    # port = 9559
    ip = "127.0.0.1"  # Virtuele robot
    # port = 52852 # laptop
    port = 59263 # pc
    move = Movement(ip, port)

    move.wake_up()
    move.freezeHead()
    move.wave()
    # move.rest()

    # waving_nao.wake_up()
    # waving_nao.wave()
    # waving_nao.rest()

#####################################################