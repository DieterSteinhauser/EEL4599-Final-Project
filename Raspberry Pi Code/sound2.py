import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('/home/sink/sinknode/Usable/mariokart.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)
