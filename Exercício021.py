# importar a biblioteca pygame
import pygame

# outra forma de implementar o código

pygame.mixer.init()
# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
pygame.mixer.music.load('thx.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar a musica...')