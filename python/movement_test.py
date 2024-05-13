from naoqi import ALProxy

# Connect to the NAO robot
nao_ip = "nao.local"  # Replace this with your NAO's IP address
nao_port = 9559
motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)
tts_proxy = ALProxy("ALTextToSpeech", nao_ip, nao_port)
autonomous_life_proxy = ALProxy("ALAutonomousLife", nao_ip, nao_port)
print("Connected to NAO robot.")

# Start autonomous life
try:
    autonomous_life_proxy.setState("solitary")
    print("Autonomous life started.")
except Exception as e:
    print("Error starting autonomous life:", e)


# Text to speech taal voor de robot
tts_proxy.setLanguage("Dutch")

# Define joint names for the arms
left_arm_joints = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
right_arm_joints = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]

# Example angles for moving the arms (in radians)
# Note: Ensure the angles are within the robot's joint limits
left_arm_angles = [0.5, 0.2, 0.3, -0.5, 0.0]  # Example angles for the left arm
right_arm_angles = [0.5, -0.2, -0.3, 0.5, 0.0]  # Example angles for the right arm

# Set angles for the arms
motion_proxy.setAngles(left_arm_joints, left_arm_angles, 0.6)  # Last argument is the speed
motion_proxy.setAngles(right_arm_joints, right_arm_angles, 0.6)  # Last argument is the speed

tts_proxy.say("Het was vrijdagavond in het gezellige Stonybrook. De ouderen verzamelden zich in het gemeenschapscentrum voor een potje bingo. Mevrouw Jenkins, met haar bril en gebloemde jurk, zat naast meneer Thompson. Het was haar tachtigste verjaardag en de sfeer was feestelijk. Ze riep Bingo! en de zaal barstte los in applaus. Na afloop vierden ze haar verjaardag met taart en lieten ze de echte schat van het leven zien: vriendschap en plezier.")