import pygame
import math

class Eye(object):
    def __init__(self, side, diameter, (x, y)):
        self.side = side
        self.diameter = diameter
        self.x = x
        self.y = y
        self.bgcolor = (0,0,0)
        self.color = (255,255,255)
        #pupil
        self.p_color = (127,127,127)
        self.p_diameter = 10
        self.p_x = x
        self.p_y = y
        self.p_state = 0 #0=still 1=moving
        self.speed = 25
        self.destx = x
        self.desty = y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), int(self.diameter/2), 0)
        pygame.draw.circle(screen, self.p_color, (self.p_x,self.p_y), int(self.p_diameter/2), 0)
        
    def moveTo(self,x,y,speed=0):
        self.destx = self.x + x
        self.desty = self.y + y
        if (speed != 0):
            self.speed = speed
        
    def updatePupil(self, speed):
        dx = self.destx - self.p_x;
        dy = self.desty - self.p_y;
        if (dx**2+dy**2 > speed**2): #
            scalefactor = math.sqrt(speed**2)/math.sqrt(dx**2+dy**2)
            dx = int(round(dx*scalefactor))
            dy = int(round(dy*scalefactor))
        self.p_x += dx    
        self.p_y += dy    

    
