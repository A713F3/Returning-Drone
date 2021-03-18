import pygame
from drone import Drone

pygame.init()
nScreenH = 500
nScreenW = 500
screen = pygame.display.set_mode([nScreenW, nScreenH])

drone = Drone(nScreenW / 2, nScreenH / 2)
drone.Start()

running = True
while running:    
    pygame.display.update()
    screen.fill((255, 255, 255))

    # Draw drone
    pygame.draw.circle(screen, (0, 0, 255), (drone.x, drone.y), 10)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        

drone.Stop()

pygame.quit()