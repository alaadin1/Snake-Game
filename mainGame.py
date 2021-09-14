import sys, pygame,random
from pygame.math import Vector2
from settings import Settings
#from snakeObj import Snake
from apple import Fruit
from snake import Snake
from pygame.math import Vector2




class SnakeGame:
    def __init__(self):

        #initialize pygame and create window
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_height))
        pygame.display.set_caption ('Snake Game')
        clock = pygame.time.Clock()

        #initilize the objects
        self.snake = Snake(self)
        self.fruit = Fruit(self)

        #set the FPS
        self.screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.screen_update,150)

        self.screen_rect = self.screen.get_rect()

        #create font object
        self.game_font = pygame.font.Font(None, 30)
        self.game_over_font = pygame.font.Font(None, 30)

        self.isAlive = True

        
    

    def run_game(self):
        #game loop consits of 
            #process input
            #update the game (screen)
            #render everything (draw everything) on the screen

        while True:
            
            #process input
            self.check_events()
            self.check_collision()
            
            
            #draw/render code
            self.screen.fill(self.settings.bg_color_white)  
            self.draw_background() 
            self.snake.draw_snake()
            self.fruit.draw_fruit()
            self.score()
            pygame.display.flip() 

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.screen_update:
                self.snake.move_snake()      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.snake.direction.y != 1:
                        self.snake.direction = Vector2(0,-1)
                elif event.key == pygame.K_DOWN:
                    if self.snake.direction.y != -1:
                        self.snake.direction = Vector2(0,1)
                elif event.key == pygame.K_RIGHT:
                    if self.snake.direction.x != -1:
                        self.snake.direction = Vector2(1,0)
                elif event.key == pygame.K_LEFT:
                    if self.snake.direction.x != 1:
                        self.snake.direction = Vector2(-1,0)

    def check_collision(self):
        #check snake collision with fruit
        if self.snake.snake_body[0] == self.fruit.pos:
            #reposition the fruit
            self.fruit.x = random.randint(0, self.settings.cell_num- 1)
            self.fruit.y = random.randint(0, self.settings.cell_num - 1)
            self.fruit.pos = Vector2(self.fruit.x,self.fruit.y)

            #add another block to the snake
            self.new_body = self.snake.snake_body[-1] 
            self.snake.snake_body.insert(-1, self.new_body)

        #check snake collision with wall
        
        #check right and left walls
        if not 0 <= self.snake.snake_body[0].x < self.settings.cell_num:
            self.isAlive = False
            self.game_over()
            


        #check top and bottom walls
        if not 0 <= self.snake.snake_body[0].y < self.settings.cell_num:
            self.isAlive = False
            self.game_over()


        #check snake collision with itself
        for block in self.snake.snake_body[1:]:
            if block == self.snake.snake_body[0]:
                self.isAlive == False
                self.game_over()

    def draw_background(self):
        grass = (152,251,152)
        darker_grass = (200,250,154)

        for row in range(self.settings.cell_num):
            if row %2 == 0:
                for col in range(self.settings.cell_num):
                    if col%2 == 0:
                        grass_rect = pygame.Rect (col*self.settings.cell_size,
                                                row*self.settings.cell_size, 
                                                self.settings.cell_size, 
                                                self.settings.cell_size)
                        pygame.draw.rect(self.screen, grass, grass_rect)

            else:
                for col in range(self.settings.cell_num):
                        if col%2 != 0:
                            grass_rect = pygame.Rect (col*self.settings.cell_size,
                                        row*self.settings.cell_size, 
                                        self.settings.cell_size, 
                                        self.settings.cell_size)
                            pygame.draw.rect(self.screen, darker_grass, grass_rect)
            
    def score(self):
        score = "Score: " + str(len(self.snake.snake_body) - 3)
        score_surface = self.game_font.render(score, True, (56,74,12))
        score_rect = score_surface.get_rect(topright = (780, 10))

        self.screen.blit(score_surface, score_rect)

    def game_over(self):
        self.snake.snake_body = [Vector2(5,10), 
                                Vector2(4,10), 
                                Vector2(3,10)]

        self.snake.direction = Vector2(0,0)

        
        game_over_txt = "GAME OVER! Press a move key to restart"
        game_over_surface = self.game_over_font.render(game_over_txt, True, (56,74,12))
        game_over_rect = game_over_surface.get_rect(center = (400, 400))

        self.screen.blit(game_over_surface, game_over_rect)
       
   #def display_gameOver(self):


if __name__ == '__main__':
    snake = SnakeGame()
    snake.run_game()