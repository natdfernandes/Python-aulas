#faça um programa em python que abra e reproduza o audio de um arquivo MP3 

import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3') #exemplo de musica
pygame.mixer.music.play()
pygame.event.wait()

