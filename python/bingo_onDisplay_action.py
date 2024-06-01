from naoqi import ALProxy

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
        self._tts_proxy.setParameter("speed", self._speed)
        self._tts_proxy(text)
        
class IdleStanding(NaoInit):
    def standing(self):
        self._posture_proxy.goToPosture("StandInit", 0.5)
        names = ["HeadYaw", "HeadPitch", "LShoulderPitch", "LShoulderRoll", 
                 "RShoulderPitch", "RShoulderRoll", "HipRoll", "HipPitch"]
        angles = [[0.5, -0.5], [0.3, -0.3], [1.0, 0.5], [0.5, -0.5], 
                  [1.0, 0.5], [-0.5, 0.5], [0.3, -0.3], [0.3, -0.3]]
        times = [[1.0, 2.0], [1.0, 2.0], [1.0, 2.0], [1.0, 2.0], 
                 [1.0, 2.0], [1.0, 2.0], [1.0, 2.0], [1.0, 2.0]]
        for name, angle, time in zip(names, angles, times):
            self._motion_proxy.angleInterpolation(name, angle, time, True)
        self.say("I love dancing!")

if __name__ == "__main__":
    ip = "127.0.0.1"  # Replace with your NAO robot's IP address
    port = 52852
    dancing_nao = DancingNao(ip)
    waving_nao = WavingNao(ip)

    dancing_nao.wake_up()
    dancing_nao.dance()
    dancing_nao.rest()

    waving_nao.wake_up()
    waving_nao.wave()
    waving_nao.rest()
