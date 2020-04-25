import pygame
import random

BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    #Ball is also a sprite

    def __init__ (self,color,width,height):
        #call the parent class constructor
        super().__init__()

        self.image=pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #Draw the ball
        pygame.draw.rect(self.image,color,(0,0,width,height))

        self.velocity=[random.randint(6,12),random.randint(-8,8)]

        self.rect=self.image.get_rect()

    def update(self):
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0]=-self.velocity[0]
        self.velocity[1]=random.randint(-8,8)
                           
    
