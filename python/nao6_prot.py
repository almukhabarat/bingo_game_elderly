from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "169.254.35.125", 9559)
motion = ALProxy( "ALMotion", "169.254.35.125", 9559)

threadMove = motion.post.moveTo( 1.0, 0.0, 0.0 )
tts.say("hi ik werk, maar ik betaal geen belasting")

motion.wait(threadMove, 0)

tts.say("jet fuel can't melt stealbeams")

