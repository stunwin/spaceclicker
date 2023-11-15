import pygame

p_number = 5
width = 1280
height = 720
locations =[]
threshold_x = .45
threshold_y = .35

def generate(width, height, number):
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            loc_x = int(i * (width / number) - (width / number / 2))
            loc_y = int(j * (height / number) - (height / number / 2))
            if loc_x > width * (1 - threshold_x) and loc_y > height * (1 - threshold_y):
                continue
            else:    
                locations.append([loc_x, loc_y])


generate(width, height, p_number)


    



pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #game go here
 

    pygame.display.flip()    
    dt = clock.tick(60) / 1000
    screen.fill("black")

    for i in locations:
        pygame.draw.polygon(screen, "blue", [(width * (1 - threshold_x), height), (width, height * (1 - threshold_y)), (width, height)])
        pygame.draw.circle(screen, "red", (locations[locations.index(i)][0], locations[locations.index(i)][1]), 40)