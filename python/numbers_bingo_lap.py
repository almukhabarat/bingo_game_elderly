import requests
import threading
from naoqi import ALProxy
import random
import cv2
import numpy as np
import vision_definitions as vd
import time


names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.176453, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.176453, [3, -0.3, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.176453, [3, -0.333333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.032256, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.032256, [3, -0.3, 0], [3, 0.333333, 0]], [-0.032256, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.032256, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.032256, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.032256, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.032256, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.032256, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.0797259, [3, -0.0333333, 0], [3, 0.3, 0]], [0.0904641, [3, -0.3, 0], [3, 0.333333, 0]], [0.0797259, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0904641, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0904641, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0904641, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0904641, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0904641, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.113474, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.113474, [3, -0.3, 0], [3, 0.333333, 0]], [-0.113474, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.113474, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.113474, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.113474, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.113474, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.113474, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.427944, [3, -0.0333333, 0], [3, 0.3, 0]], [-1.22562, [3, -0.3, 0], [3, 0.333333, 0]], [-1.15813, [3, -0.333333, -0.0674953], [3, 0.333333, 0.0674953]], [-0.608956, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.4864, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.20261, [3, -0.333333, -0.169763], [3, 0.333333, 0.169763]], [-0.467829, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.52322, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-1.17969, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.770109, [3, -0.3, 0], [3, 0.333333, 0]], [-1.15208, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.995607, [3, -0.333333, -0.0350264], [3, 0.333333, 0.0350264]], [-0.941918, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.2748, [3, -0.333333, 0.0920399], [3, 0.333333, -0.0920399]], [-1.49416, [3, -0.333333, 0.0122732], [3, 0.333333, -0.0122732]], [-1.50643, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.237757, [3, -0.0333333, 0], [3, 0.3, 0]], [0.0232, [3, -0.3, -0.0018], [3, 0.333333, 0.002]], [0.0252, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0232, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0232, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0140001, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0140001, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0232, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.136568, [3, -0.0333333, 0], [3, 0.3, 0]], [0.12583, [3, -0.3, 0], [3, 0.333333, 0]], [0.136568, [3, -0.333333, 0], [3, 0.333333, 0]], [0.12583, [3, -0.333333, 0], [3, 0.333333, 0]], [0.12583, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136568, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136568, [3, -0.333333, 0], [3, 0.333333, 0]], [0.12583, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.11049, [3, -0.0333333, 0], [3, 0.3, 0]], [0.11049, [3, -0.3, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.170232, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.170232, [3, -0.3, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.0874801, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.0874801, [3, -0.3, 0], [3, 0.333333, 0]], [-0.0874801, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0874801, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0874801, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0874801, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0874801, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0874801, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[1.52322, [3, -0.0333333, 0], [3, 0.3, 0]], [1.42504, [3, -0.3, 0.0574041], [3, 0.333333, -0.0637823]], [1.15966, [3, -0.333333, 0.0649393], [3, 0.333333, -0.0649393]], [1.03541, [3, -0.333333, 0], [3, 0.333333, 0]], [1.15506, [3, -0.333333, 0], [3, 0.333333, 0]], [0.766959, [3, -0.333333, 0.108147], [3, 0.333333, -0.108147]], [0.506179, [3, -0.333333, 0], [3, 0.333333, 0]], [1.03234, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.16563, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.0951499, [3, -0.3, 0.0685457], [3, 0.333333, -0.0761619]], [-0.268493, [3, -0.333333, 0.0370717], [3, 0.333333, -0.0370717]], [-0.31758, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.092082, [3, -0.333333, -0.0756774], [3, 0.333333, 0.0756774]], [0.136484, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0583338, [3, -0.333333, 0.039117], [3, 0.333333, -0.039117]], [-0.0982179, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.122678, [3, -0.0333333, 0], [3, 0.3, 0]], [1.46953, [3, -0.3, -0.0566036], [3, 0.333333, 0.0628929]], [1.53242, [3, -0.333333, 0], [3, 0.333333, 0]], [1.49868, [3, -0.333333, 0.0337477], [3, 0.333333, -0.0337477]], [1.14892, [3, -0.333333, 0], [3, 0.333333, 0]], [1.16733, [3, -0.333333, -0.018408], [3, 0.333333, 0.018408]], [1.61066, [3, -0.333333, 0], [3, 0.333333, 0]], [1.45112, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.0859461, [3, -0.0333333, 0], [3, 0.3, 0]], [0.0859461, [3, -0.3, 0], [3, 0.333333, 0]], [0.0859461, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0859461, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0859461, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0859461, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0859461, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0859461, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.11049, [3, -0.0333333, 0], [3, 0.3, 0]], [0.11049, [3, -0.3, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0.333333, 0]], [0.11049, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.412688, [3, -0.0333333, 0], [3, 0.3, 0]], [0.412688, [3, -0.3, 0], [3, 0.333333, 0]], [0.412688, [3, -0.333333, 0], [3, 0.333333, 0]], [0.412688, [3, -0.333333, 0], [3, 0.333333, 0]], [0.412688, [3, -0.333333, 0], [3, 0.333333, 0]], [0.412688, [3, -0.333333, 0], [3, 0.333333, 0]], [0.412688, [3, -0.333333, 0], [3, 0.333333, 0]], [0.412688, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[1.20722, [3, -0.0333333, 0], [3, 0.3, 0]], [1.20722, [3, -0.3, 0], [3, 0.333333, 0]], [1.20722, [3, -0.333333, 0], [3, 0.333333, 0]], [1.20722, [3, -0.333333, 0], [3, 0.333333, 0]], [1.20722, [3, -0.333333, 0], [3, 0.333333, 0]], [1.20722, [3, -0.333333, 0], [3, 0.333333, 0]], [1.20722, [3, -0.333333, 0], [3, 0.333333, 0]], [1.20722, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.3144, [3, -0.0333333, 0], [3, 0.3, 0]], [0.3144, [3, -0.3, 0], [3, 0.333333, 0]], [0.3144, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3144, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3144, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3144, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3144, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3144, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.130348, [3, -0.0333333, 0], [3, 0.3, 0]], [0.130348, [3, -0.3, 0], [3, 0.333333, 0]], [0.130348, [3, -0.333333, 0], [3, 0.333333, 0]], [0.130348, [3, -0.333333, 0], [3, 0.333333, 0]], [0.130348, [3, -0.333333, 0], [3, 0.333333, 0]], [0.128814, [3, -0.333333, 0], [3, 0.333333, 0]], [0.141086, [3, -0.333333, 0], [3, 0.333333, 0]], [0.130348, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.110406, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.110406, [3, -0.3, 0], [3, 0.333333, 0]], [-0.121144, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.110406, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.110406, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.121144, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.121144, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.121144, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.170232, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.170232, [3, -0.3, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.170232, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.0812599, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.093532, [3, -0.3, 0], [3, 0.333333, 0]], [-0.093532, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.093532, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.093532, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.093532, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.093532, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.093532, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[1.5187, [3, -0.0333333, 0], [3, 0.3, 0]], [1.5187, [3, -0.3, 0], [3, 0.333333, 0]], [1.5187, [3, -0.333333, 0], [3, 0.333333, 0]], [1.5187, [3, -0.333333, 0], [3, 0.333333, 0]], [1.5187, [3, -0.333333, 0], [3, 0.333333, 0]], [1.5187, [3, -0.333333, 0], [3, 0.333333, 0]], [1.5187, [3, -0.333333, 0], [3, 0.333333, 0]], [1.5187, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[-0.165714, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.06447, [3, -0.3, -0.0193283], [3, 0.333333, 0.0214759]], [-0.0429941, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.06447, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.06447, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.047596, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.047596, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.06447, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0, 0.9, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9])
keys.append([[0.136484, [3, -0.0333333, 0], [3, 0.3, 0]], [0.136484, [3, -0.3, 0], [3, 0.333333, 0]], [0.136484, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136484, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136484, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136484, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136484, [3, -0.333333, 0], [3, 0.333333, 0]], [0.136484, [3, -0.333333, 0], [3, 0, 0]]])








class DatabaseHandler:
    def __init__(self, db_url):
        self.db_url = db_url

    def post_request(self, data):
        try:
            response = requests.post(self.db_url, data=data)
            response.raise_for_status()  # Raises an error for bad status codes
        except requests.exceptions.RequestException as e:
            print('Failed to send data: {}'.format(e))
            return None

class BingoSpel(DatabaseHandler):
    def __init__(self, ip="127.0.0.1", port=58600):
        DatabaseHandler.__init__(self, "http://145.92.8.134/bingo_db_post.php")
        self.ip = ip
        self.port = port
        self.speech_proxy = ALProxy("ALTextToSpeech", ip, port)
        self.autonomous_life_proxy = ALProxy("ALAutonomousLife", ip, port)
        self.posture_proxy = ALProxy("ALRobotPosture", ip, port)
        self.motion_proxy = ALProxy("ALMotion", ip, port)
        self.language = "Dutch"
        self.speed = 100
        self.speech_proxy.setLanguage(self.language)
        self.speech_proxy.setParameter("speed", self.speed)
        self.opgeroepen_nummers = []
        self.spel_running = False
        self.game_thread = None
        self.qr_thread = None
        self.bingo_spel_id = None
        self.qr_code_numbers = []  # To store numbers from the bingo card
        self.ball_ready_event = threading.Event()  # Event to signal when the ball is ready

        # Start polling for commands in separate threads
        self.command_thread = threading.Thread(target=self.poll_command, args=("http://145.92.8.134/bingoknop_api/get", self.handle_command_response))
        self.ball_position_thread = threading.Thread(target=self.poll_command, args=("http://145.92.8.134/bingobal_api/get", self.handle_ball_response))

        self.command_thread.start()
        self.ball_position_thread.start()

    def new_game_db(self):
        post_game_begin = {
            'query_type': 'post_game_begin',
        }
        response_json = self.post_request(post_game_begin)
        if response_json:
            self.bingo_spel_id = response_json.get('bingoSpelId')
            print('Data sent successfully: {}'.format(response_json))

    def save_number_to_db(self, number):
        if self.bingo_spel_id is not None:
            post_number = {
                'query_type': 'post_number',
                'bingoSpelId': self.bingo_spel_id,
                'opgenoemd': number
            }
            response_json = self.post_request(post_number)
            if response_json:
                print('Number saved successfully: {}'.format(response_json))

    def fetch_bingo_card(self, bingo_kaart_id):
        post_data = {
            'query_type': 'get_bingo_card',
            'bingoKaartId': bingo_kaart_id
        }
        response_json = self.post_request(post_data)
        if response_json:
            if 'error' in response_json:
                print('Error fetching bingo card: {}'.format(response_json['error']))
            else:
                card_numbers = response_json.get('getal')
                if card_numbers:
                    self.qr_code_numbers = list(map(int, card_numbers.split(',')))
                    print('Fetched Bingo Card Numbers: {}'.format(self.qr_code_numbers))
                else:
                    print('Failed to fetch bingo card numbers.') 
        else:
            print('Failed to fetch bingo card.')

    def start_spel(self):
        # Wake up the robot
        self.motion_proxy.wakeUp()
        # Make the robot stand
        self.posture_proxy.goToPosture("StandInit", 0.5)

        self.new_game_db()

        self.speech_proxy.say("Welkom bij Bingo!")
        self.spel_running = True
        if self.game_thread is None or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=self.speel_bingo)
            self.game_thread.start()

    def stop_spel(self):
        self.spel_running = False
        if self.game_thread is not None:
            self.game_thread.join()

    def resume_spel(self):
        self.spel_running = True
        if self.game_thread is None or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=self.speel_bingo)
            self.game_thread.start()

    def poll_command(self, url, handler):
        while True:
            try:
                response = requests.get(url)
                response.raise_for_status()
                handler(response.json())
            except requests.exceptions.RequestException as e:
                print("HTTP Request failed ({url}): {e}")

    def handle_command_response(self, response_json):
        command = response_json.get('command', None)
        
        if command == 'bingo':
            print("bingo called")
            self.stop_spel()
            self.hoofd_stil(True)  # Houdt hoofd stil zodat qr code eenvoudig gescanned kan worden

            if self.qr_thread is None or not self.qr_thread.is_alive():
                self.qr_thread = threading.Thread(target=self.start_qr_detection)
                self.qr_thread.start()

        elif command == 'start':
            print("game starting")
            self.start_spel()
            self.hoofd_stil(False)

    def handle_ball_response(self, response_json):
        command = response_json.get('command', None)
        
        if command == 'bal op positie':
            print("Command received: bal op positie")
            self.ball_ready_event.set()  # Signal that the ball is ready

    def roep_nummer_op(self):
        while self.spel_running:
            nummer = random.randint(1, 19)
            if nummer not in self.opgeroepen_nummers:
                self.opgeroepen_nummers.append(nummer)  # game houdt zelf bij welke nummers zijn omgeroepen
                
                self.save_number_to_db(nummer)

                self.draai_molen()
                self.speech_proxy.say("Het volgende nummer is {}".format(nummer))
                time.sleep(1)
                self.speech_proxy.say(str(nummer))
                time.sleep(0.5)
                return nummer
            
    def draai_molen(self):
        data = {
            "command": "Draaien pls"
        }
        try:
            print("Sending POST request to start the wheel turning...")
            response = requests.post('http://145.92.8.134/bingobal_api/post', json=data)
            response.raise_for_status()
            print("POST request sent successfully: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            print('Failed to send POST request: {}'.format(e))
            return
        
        print("Waiting for ball to be ready...")
        self.ball_ready_event.wait()  # Wait for the event to be set
        print("Ball is ready!")
        # Call angleInterpolationBezier with the variables from movement_coordinates module
        self.motion_proxy.angleInterpolationBezier(names, times, keys)
        self.ball_ready_event.clear()  # Clear the event for the next round

    def speel_bingo(self):
        while self.spel_running:
            nummer = self.roep_nummer_op()
            time.sleep(4)

    def controleer_winst(self):
        # 3x3 grid win conditions
        win_conditions = [
            # Rows
            [0, 1, 2], 
            [3, 4, 5], 
            [6, 7, 8],
            # Columns
            [0, 3, 6], 
            [1, 4, 7], 
            [2, 5, 8],
            # Diagonals
            [0, 4, 8], 
            [2, 4, 6]
        ]
        
        print("Checking win conditions")
        print("Called numbers: {}".format(self.opgeroepen_nummers))
        print("QR code numbers: {}".format(self.qr_code_numbers))

        if len(self.qr_code_numbers) != 9:
            print("Invalid bingo card size.")
            return False
        
        for condition in win_conditions:
            condition_numbers = [self.qr_code_numbers[i] for i in condition]
            print("Checking condition: {} -> {}".format(condition, condition_numbers))
            
            if all(number in self.opgeroepen_nummers for number in condition_numbers):
                print("Winning condition met: {}".format(condition))
                return True

        print("No winning condition met.")
        self.resume_spel()
        return False
    
    def start_qr_detection(self):

        # Initialize the video service
        self.video_service = ALProxy("ALVideoDevice", self.ip, self.port)
    
        resolution = vd.kVGA
        color_space = vd.kRGBColorSpace
        fps = 20
        camera_index = 0
        video_client = self.video_service.subscribeCamera("python_client", camera_index, resolution, color_space, fps)
        print("QR detection started")

        qr_detector = cv2.QRCodeDetector()

        try:
            while True:
                nao_image = self.video_service.getImageRemote(video_client)
                if nao_image is None:
                    print("Kon geen afbeelding van de camera krijgen.")

                image_width = nao_image[0]
                image_height = nao_image[1]
                array = nao_image[6]
                image = np.frombuffer(array, dtype=np.uint8).reshape((image_height, image_width, 3))
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                data, bbox, _ = qr_detector.detectAndDecode(image)

                if bbox is not None and data:
                    print("QR Code Detected:")
                    print(data)
                    self.fetch_bingo_card(int(data))  # Fetch the bingo card numbers using the bingoKaartId

                    # Check for win after scanning the QR code
                    if self.controleer_winst():
                        self.speech_proxy.say("Bingo! We hebben een winnaar!")
                    else:
                        self.speech_proxy.say("Geen Bingo! Probeer opnieuw.")
                    break

                time.sleep(1)
        finally:
            self.video_service.unsubscribe(video_client)
            cv2.destroyAllWindows()

    # Deze functie kan later nog in een aparte movement class komen
    def hoofd_stil(self, freeze):
        # Positioneerd hoofdpositie naar voren
        if freeze:
            head_joints = ["HeadYaw", "HeadPitch"]
            angles = [0.0, 0.0]  # 0.0, hoofd is gecentreerd
            fractionMaxSpeed = 0.1
            self.motion_proxy.setAngles(head_joints, angles, fractionMaxSpeed)

            # Stijfheid van het hoofd
            stiffness = 1.0 if freeze else 0.0
            self.motion_proxy.setStiffnesses(head_joints, stiffness)

def main():
    bingo_spel = BingoSpel()

if __name__ == "__main__":
    main()