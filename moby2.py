import pygame
#import RPi.GPIO as GPIO
import time
import moby

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 14)
screen = pygame.display.set_mode((1024, 600))
bgcolor = (0,0,0);
screen.fill(bgcolor)
done = False
speed = 10
statusmessage = ''

eyedirs = {pygame.K_q:[-85,-85],pygame.K_w:[0,-120],pygame.K_e:[85,-85],pygame.K_a:[-120,0],pygame.K_s:[0,0],pygame.K_d:[120,0],pygame.K_z:[-85,85],pygame.K_x:[0,120],pygame.K_c:[85,85]}

l_eye = moby.Eye("left", 325, (200, 200))
l_eye.draw(screen)

r_eye = moby.Eye("right", 325, (824, 200))
r_eye.draw(screen)

def moveEyes(x,y, speed=0, l_eye=l_eye, r_eye=r_eye):
    l_eye.moveTo(x,y,speed)
    r_eye.moveTo(x,y,speed)

    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True 
            elif event.key in eyedirs:
                moveEyes(eyedirs[event.key][0],eyedirs[event.key][1],speed)

    if (statusmessage):
        status = myfont.render(statusmessage,False,(255,0,0))
        screen.blit(status, (10,10))
        
    l_eye.updatePupil(speed)
    r_eye.updatePupil(speed) 
    l_eye.draw(screen)
    r_eye.draw(screen)
    pygame.display.flip()    
    time.sleep(.03)
    

    