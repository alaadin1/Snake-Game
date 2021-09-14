import pygame,random
from pygame.math import Vector2

class Fruit:
    def __init__(self,snake_game):
        self.screen = snake_game.screen
        self.settings = snake_game.settings
        self.cell_size = self.settings.cell_size
        self.cell_num = self.settings.cell_num

        self.x = random.randint(0, self.cell_num- 1)
        self.y = random.randint(0, self.cell_num - 1)
        self.pos = Vector2(self.x,self.y)

        self.color = (142, 209, 80)

        self.apple = pygame.image.load('/Users/Alaa/Desktop/python_work/Projects/Snake Game/image/apple.png').convert_alpha()
 
    def draw_fruit(self):
        #create rectangle
        self.fruit = pygame.Rect(int(self.pos.x*self.cell_size), 
                                int(self.pos.y*self.cell_size), 
                                self.cell_size, 
                                self.cell_size )

        #draw rectangle
        #pygame.draw.rect(self.screen, self.color, self.fruit)
        self.screen.blit(self.apple, self.fruit)