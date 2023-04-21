import thingspeak
import pygame
import random

def parseID(idnum, data):
	#print(f'ID: "{idnum}" is {str(idnum) == "0013A20041D6E99C"}')
	#print(type(idnum))
	
	if int(data) > 250:
		pygame.mixer.init()
		sound = pygame.mixer.Sound('/home/sink/sinknode/Usable/beep' + str(random.randint(1, 10)) +'.wav')
		playing = sound.play()
		while playing.get_busy():
			pygame.time.delay(100)
	
	
	if str(idnum)  == "0013A20041D6E99C":
		print("sending to field1")
		thingspeak.send(data, 'field1', "2FXIAZTDLKSROT3W")
	else: 
		print("sending to field2")
		thingspeak.send(data, 'field2', "2FXIAZTDLKSROT3W")
