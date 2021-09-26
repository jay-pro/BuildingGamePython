import pygame
from random import randint

black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    """docstring for ClassName"""
    #This class represents a car. It derives from the "Sprite" class in Pygame

    def __init__(self,color,width,height):
        #Call the parent class (Sprite) constructor
        super().__init__()

        #Pass in the color of the car, and its x and y position, width and height.
        #Set the backgrounf color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        #Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.velocity = [randint(4,8),randint(-8,8)]

        #Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bouncing(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = self.velocity[1]