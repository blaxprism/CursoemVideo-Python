import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('files/transcender.mp3')
pygame.mixer.music.play()
pygame.event.wait()
