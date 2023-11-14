# Example file showing a circle moving on screen
import pygame
import numpy as np
from random import randint
import math

def disty(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)
    
class Planet:   
    def __init__(self, name):
        self.x = randint(100, 1180)
        self.y = randint(100, 620)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.name = name  
        self.titlesurf = font.render(self.name, True, self.color)
    
    def draw(self):
        screen.blit(self.titlesurf, (self.x - self.titlesurf.get_width()/2, self.y + 42))
        if disty(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.x, self.y) < 40:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 40, width = 10)
            if pygame.mouse.get_pressed()[0]:
                self.x = pygame.mouse.get_pos()[0]
                self.y = pygame.mouse.get_pos()[1]
            return
        pygame.draw.circle(screen, self.color, (self.x, self.y), 40)
                        


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Lato", 12)




planetNames = ["alderaan", "magrathea", "omecron", "t1", "t2", "t3"]
planetList = []

#spawn stuff
for i in planetNames:
    planetList.append(Planet(i))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #game go here

    pygame.display.flip()    
    dt = clock.tick(60) / 1000
    screen.fill("black")
    
    #draw lines between planets in order
    for i in range(0, len(planetList)): 
        j = i + 1
        if j > len(planetList) - 1:
            j = 0                
        pygame.draw.aaline(screen, "white", (planetList[i].x, planetList[i].y), (planetList[j].x, planetList[j].y))
    
    #draw planets
    for i in planetList:
        i.draw()
    
    
    
    
pygame.quit()
sys.exit()
