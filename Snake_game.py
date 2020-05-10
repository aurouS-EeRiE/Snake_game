"""
Created on Sat May  9 23:36:16 2020

Title: Snake Game

@author: aurouS_EeRiE
"""


import pygame
import sys
import time
import random
import winsound
pygame.init()

x_dist = 800
y_dist = 600

frequency = 3000
duration = 100

clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

dis = pygame.display.set_mode((x_dist, y_dist))
pygame.display.update()

pygame.display.set_caption("Snake Game - aurouS_EeRiE")

background = (0, 0, 0)
snake_color = (255, 254, 255)
text_color = (0, 255, 0)
score_color = (255, 0, 0)
lose_background = (0, 0, 0)

appleimg = pygame.image.load('D:\\Documents\\Addepalli\\Spyder\\apple.png')

font_style = pygame.font.SysFont("comicsansms", 35)
score_font = pygame.font.SysFont("bahnschrift", 30)

def message(msg, color):
    msgg = font_style.render(msg, True, color)
    dis.blit(msgg, [x_dist/6, y_dist/3])

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, score_color)
    dis.blit(value, [0, 0])
 
def gameloop():
    game_over = False
    game_close = False
    
    x1 = x_dist/2
    y1 = y_dist/2
    
    x1_change = 0
    y1_change = 0
    
    snake_length = 1
    snake_list = []
    
    foodx = round(random.randrange(0, x_dist - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, y_dist - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close == True:
            time.sleep(1)
            dis.fill(lose_background)
            message("You Lost! Press C-Play Again or Q-Quit", text_color)
            Your_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    
        x1 += x1_change
        y1 += y1_change
        dis.fill(background)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
                
        my_snake(snake_block, snake_list)
        Your_score(snake_length - 1)
                        
                    
        if x1 >= x_dist or x1 < 0 or y1 >= y_dist or y1 < 0:
            game_close = True
                    
        dis.blit(appleimg, (foodx, foody))
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, x_dist - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, y_dist - snake_block) / 10.0) * 10.0
            winsound.Beep(frequency, duration)
            snake_length += 1
        
        clock.tick(snake_speed)
        
    pygame.quit()
    sys.exit()
gameloop()