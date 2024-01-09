## Reprodução arquivo musica local
import pygame

pygame.init()
pygame.mixer.music.load('c:\Users\User\Music\EM thirds v1.1.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()