from naoqi import ALProxy
import time

class NaoRobot:
    def __init__(self, ip, port):
        # de NaoRobot met IP-adres en port
        self.nao_ip = ip
        self.nao_port = port
        # Creëer proxies voor beweging, autonomie en tekst-naar-spraak
        self.motion_proxy = ALProxy("ALMotion", self.nao_ip, self.nao_port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", self.nao_ip, self.nao_port)
        self.tts_proxy = ALProxy("ALTextToSpeech", self.nao_ip, self.nao_port)
        # Stel taal en snelheid in voor de robot
        self.language = "Dutch"
        self.speed = 80
        self.tts_proxy.setLanguage(self.language)
        self.tts_proxy.setParameter("speed", self.speed)
        
    def turn_robot(self, angle):
        # Draai de robot 
        self.motion_proxy.moveTo(0, 0, angle)
        
    def move_arms(self, left_angles, right_angles):
        # Beweeg de armen van de robot naar de opgegeven gewrichtshoeken
        self.motion_proxy.setAngles("LArm", left_angles, 0.5)
        self.motion_proxy.setAngles("RArm", right_angles, 0.5)
        
    def wave(self):
        # Implementeer de zwaaiende beweging van de robot
        
    #def start_autonomous_life(self):
        try:
            # Start de autonomie van de robot
            self.autonomous_life_proxy.setState("solitary")
            print("Autonomous life started.")
        except Exception as e:
            print("Error starting autonomous life:", e)
    
    def say(self, text):
        # zodat nao praten
        self.tts_proxy.say(text)

# Voorbeeldgebruik:
if __name__ == "__main__":
    # connectie mrt de robot via port
    nao_robot = NaoRobot("nao.local", 9559)
    # Start de autonomy van de robot
    nao_robot.start_autonomous_life()
    # Draai de robot
    nao_robot.turn_robot(-1.57)
    # Beweeg de armen van de robot
    left_arm_angles = [0.5, 0.5, -1.0, 0.5, 0.5, 0.5]
    right_arm_angles = [-0.5, -0.5, 1.0, -0.5, -0.5, -0.5]
    nao_robot.move_arms(left_arm_angles, right_arm_angles)
    time.sleep(2)
    nao_robot.say("Hi ik ben NAO. Dit is Ana, Brian, Tyler, Tess en Amin en ons project gaat over mij inzetten zodat ik bingo kan spelen met de ouderen die in het amstelhuis wonen. Ik noem de cijfers op en zij kleuren de cijfers in tot dat ze bingo hebben. Dan ga ik checken of dat ook zo is")
    time.sleep(5) 
