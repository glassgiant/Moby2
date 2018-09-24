import pygame
#import RPi.GPIO as GPIO
import time
import moby

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.init()
screen = pygame.display.set_mode((700, 300))
done = False

l_eye = moby.Eye("left", 200, (150, 150))
l_eye.draw(screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_a:
                l_eye.moveTo(-95,0)
            elif event.key == pygame.K_s:
                l_eye.moveTo(0,0,5)
            elif event.key == pygame.K_d:
                l_eye.moveTo(95,0,5)
    
    l_eye.updatePupil()
    l_eye.draw(screen)
    time.sleep(.01)