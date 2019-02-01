import pygame

pygame.init()
pygame.joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print("le bouton du joystick a été appuyé")
        if event.type == pygame.JOYBUTTONUP:
            print("le bouton a été relaché")
