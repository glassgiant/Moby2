import pygame

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
        screen.fill(self.bgcolor)
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.diameter/2, 0)
        pygame.draw.circle(screen, self.p_color, (self.p_x,self.p_y), self.p_diameter/2, 0)
        pygame.display.flip()
        
    def moveTo(self,x,y,speed=0):
        self.destx = self.x + x
        self.desty = self.y + y
        if (speed != 0)
            self.speed = speed
        
    def updatePupil(self):
        dx = self.destx - self.p_x;
        if (dx < -self.speed):
            dx = -self.speed
        elif (dx > self.speed):
            dx = self.speed
        dy = self.desty - self.p_y;
        if (dy < -self.speed):
            dy = -self.speed
        elif (dy > self.speed):
            dy = self.speed
        self.p_x += dx    
        self.p_y += dy    

    
