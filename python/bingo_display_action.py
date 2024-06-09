from naoqi import ALProxy
import time

class NaoInit:
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self._language = "Dutch"
        self._tts_speed = 100
        self._motion_proxy = ALProxy("ALMotion", self._ip, self._port)
        self._posture_proxy = ALProxy("ALRobotPosture", self._ip, self._port)
        self._tts_proxy = ALProxy("ALTextToSpeech", self._ip, self._port)
        self._face_detection_proxy = ALProxy("ALFaceDetection", self._ip, self._port)
        self._memory_proxy = ALProxy("ALMemory", self._ip, self._port)
        self._tracker_proxy = ALProxy("ALTracker", self._ip, self._port)
        self._life_proxy = ALProxy("ALAutonomousLife", self._ip, self._port)

    def wake_up(self):
        self._motion_proxy.wakeUp()
        self.enable_autonomous_life()

    def rest(self):
        self._motion_proxy.rest()
    
    def speech(self, text):
        self._tts_proxy.setLanguage(self._language)
        self._tts_proxy.setParameter("speed", self._tts_speed)
        self._tts_proxy.say(text)

    def enable_autonomous_life(self):
        self._life_proxy.setState("interactive")
        
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
    
    def look_around(self):
        self._face_detection_proxy.subscribe("Test_Face", 500, 0.0)
        time.sleep(1)

        while True:
            face_data = self._memory_proxy.getData("FaceDetected")
            if face_data and isinstance(face_data, list) and len(face_data) > 0:
                move.wave()
                self.speech("Hallo, wil jij bingo met mij spelen?")
                self.enable_autonomous_life()
                self.track_face(str(face_data[0][0]))  # Convert face_id to string before tracking
                break  # Exit the loop and let autonomous life take over
            else:
                self.enable_autonomous_life()
                break

    def track_face(self, face_id):
        target_name = "Face"
        face_width = 0.1  # Width of the face in meters
        self._tracker_proxy.registerTarget(target_name, face_width)
        self._tracker_proxy.track(target_name)
        self._tracker_proxy.setMode("Head")  # Set tracking mode to "Head" for head movement tracking
        self._tracker_proxy.track(face_id)  # Start tracking the specified face

def main_loop():
    ip = "127.0.0.1"  # NAO robot via ethernet
    port = 61945
    move = Movement(ip, port)
    move.wake_up()

    while True:
        move.look_around()
        # move.wave()
        time.sleep(20)  # Look around once every 60 seconds


if __name__ == "__main__":
    main_loop()

#####################################################