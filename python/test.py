from naoqi import ALProxy

nao_ip = "nao.local"  # Replace with your NAO's IP address
nao_port = 9559  # Default port for NAO

asr = ALProxy("ALSpeechRecognition", nao_ip, nao_port)

asr.setLanguage("Dutch")

vocabulary = ["ja", "nee", "bingo"]
asr.setVocabulary(vocabulary, False)

asr.subscribe("Test_ASR")
print 'Speech recognition started.'
time.sleep(20)
asr.unsubscribe("Test_ASR")
