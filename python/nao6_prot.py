from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "169.254.30.75", 9559)
motion = ALProxy( "ALMotion", "169.254.30.75", 9559)

threadMove = motion.post.moveTo( 1.0, 0.0, 0.0 )
tts.say("hi ik werk")

motion.wait(threadMove, 0)

tts.say("hi ik werk")

