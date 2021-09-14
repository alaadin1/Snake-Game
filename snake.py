import pygame
from pygame.math import Vector2

class Snake:
    def __init__ (self,snake_game):
        self.screen = snake_game.screen
        self.settings = snake_game.settings
        self.cell_size = self.settings.cell_size
        self.cell_num = self.settings.cell_num

        #import snake images
        self.head_up = pygame.image.load('image/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('image/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('image/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('image/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('image/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('image/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('image/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('image/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('image/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('image/body_horizontal.png').convert_alpha()
        
        self.body_topright = pygame.image.load('image/body_topright.png').convert_alpha()
        self.body_topleft = pygame.image.load('image/body_topleft.png').convert_alpha()
        self.body_bottomright = pygame.image.load('image/body_bottomright.png').convert_alpha()
        self.body_bottomleft = pygame.image.load('image/body_bottomleft.png').convert_alpha()
        
        self.snake_body = [Vector2(5,10), 
                           Vector2(4,10), 
                           Vector2(3,10)]
        self.direction = Vector2(0,0)

    def draw_snake(self):
        #create the snake body based on the images imported
        self.head = self.head_left
        self.update_head()

        for index, block in enumerate(self.snake_body):
            #Need a rect for the positioning
            self.x_pos = int(block.x * self.cell_size)
            self.y_pos = int(block.y * self.cell_size)

            self.body_rect = pygame.Rect(self.x_pos, 
                                        self.y_pos, 
                                        self.cell_size, 
                                        self.cell_size)

            #Update the snake's head
            if index == 0:
                self.screen.blit(self.head,self.body_rect)

            #update the snakes tail
            elif index == len(self.snake_body) - 1:
                tail_vector = self.snake_body[-2] - self.snake_body[-1]

                if tail_vector == Vector2(1,0): 
                    self.screen.blit(self.tail_left, self.body_rect)
                elif tail_vector == Vector2(-1,0): 
                    self.screen.blit(self.tail_right, self.body_rect)
                elif tail_vector == Vector2(0,1): 
                    self.screen.blit(self.tail_up, self.body_rect)
                elif tail_vector == Vector2(0,-1): 
                    self.screen.blit(self.tail_down, self.body_rect)

            #update the snakes body
            else:
                prev = self.snake_body[index + 1] - block
                nxt = self.snake_body[index - 1] - block

                #horiz/vertical body parts
                if prev.x == nxt.x:
                    self.screen.blit(self.body_vertical, self.body_rect)
                elif prev.y == nxt.y:
                    self.screen.blit(self.body_horizontal, self.body_rect)

                #corner of the bodies
                else:
                    if prev.x == -1 and nxt.y == -1 or prev.y == -1 and nxt.x == -1:
                        self.screen.blit(self.body_topleft, self.body_rect)
                    elif prev.x == -1 and nxt.y == 1 or prev.y == 1 and nxt.x == -1:
                        self.screen.blit(self.body_bottomleft, self.body_rect)
                    elif prev.x == 1 and nxt.y == -1 or prev.y == -1 and nxt.x == 1:
                            self.screen.blit(self.body_topright, self.body_rect)    
                    elif prev.x == 1 and nxt.y == 1 or prev.y == 1 and nxt.x == 1:
                            self.screen.blit(self.body_bottomright, self.body_rect)
  
    def move_snake(self):
        #The logic to move the snake is that we will create a direction var
        #This direction var will be where we create the new 'head' (0th index) of the snake 
        #We then will move the prev prev 0Th and 1st index up one while deleteing the last index
        self.copy_body = self.snake_body[:-1]
        self.copy_body.insert(0,self.copy_body[0]+self.direction)
        self.snake_body = self.copy_body[:]

    def update_head(self):
        head_vector = self.snake_body[1] - self.snake_body[0]
        #update the screen heads position
        if head_vector == Vector2(1,0):
            self.head = self.head_left
        elif head_vector == Vector2(-1,0):
            self.head = self.head_right
        elif head_vector == Vector2(0,1):
            self.head = self.head_up
        elif head_vector == Vector2(0,-1):
            self.head = self.head_down