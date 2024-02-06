import random
import sys

import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10) , Vector2(4,10) , Vector2(3,10)]
        self.direction = Vector2(0,1)
        self.new_block = False
        

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect = pygame.Rect(x_pos , y_pos , cell_size , cell_size )
            pygame.draw.rect(screen,(255,30,150),block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] 
            body_copy.insert(0,body_copy[0]+self.direction)      
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] 
            body_copy.insert(0,body_copy[0]+self.direction)      
            self.body = body_copy[:]

    def add_block(self):    
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,10) , Vector2(4,10) , Vector2(3,10)]    

class Fruit:
    def __init__(self):
        self.randomize()
 
    def draw_fruit(self):  
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size) , int(self.pos.y*cell_size) , cell_size , cell_size)   
        screen.blit(apple,fruit_rect)
        

    def randomize(self):
        self.x = random.randint(0,cell_no-1)
        self.y = random.randint(0,cell_no-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_element(self):
        self.fruit.draw_fruit() 
        self.snake.draw_snake()  
        self.draw_score()  

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos :
                self.fruit.randomize()

    def check_fail(self):
        if not 0<=self.snake.body[0].x<cell_no or not 0<=self.snake.body[0].y<cell_no  :
            self.game_over() 
        for block in self.snake.body[1:] :
            if block == self.snake.body[0] :
                self.gameover()  

    def game_over(self):
        self.snake.reset()


    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size*cell_no-60)
        score_y = int(cell_size*cell_no-40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top, apple_rect.width+score_rect.width+30, apple_rect.height)

        pygame.draw.rect(screen,(255,180,132), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(255,255,255), bg_rect,2)

   
pygame.init()
cell_size = 40
cell_no = 20
screen = pygame.display.set_mode((cell_no*cell_size, cell_no*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('apple.png').convert_alpha()
game_font = pygame.font.Font(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)                                            
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)


    screen.fill((175,121,225))  
    main_game.draw_element()
    pygame.display.update()
    clock.tick(60)       
