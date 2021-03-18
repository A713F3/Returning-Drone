import pygame
import threading

class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.speed = 0.1

        self.keep = True
    
    def Start(self):
        self.keep = True

        axisx_thread = threading.Thread(target=self.AxisX)
        axisx_thread.start()


    def Stop(self):
        self.keep = False


    def AxisX(self):
        while self.keep:
            keys = pygame.key.get_pressed()
            #self.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
            if keys[pygame.K_RIGHT]:
                self.x += self.speed

            if keys[pygame.K_RIGHT]:
                self.x -= self.speed
    

