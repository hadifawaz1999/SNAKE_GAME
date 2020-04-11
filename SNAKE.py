import pygame
import time
import random

pygame.init()

clock=pygame.time.Clock()

red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)

w_screen=800
h_screen=600
snake_size=10
win=pygame.display.set_mode((w_screen,h_screen))
win.fill(black)
pygame.display.set_caption("snake")

font_style=pygame.font.SysFont(None,50)
speed=10

def message(s,color):
    mseg=font_style.render(s,True,color)
    win.blit(mseg,[w_screen/12,h_screen/2])

def show_score(score,color):
    mseg=font_style.render("Score: "+str(score),True,color)
    win.blit(mseg,[10,10])

def play_game():
    score=0
    game_over=False
    game_close=False
    x=w_screen/2
    y=h_screen/2
    add_x=0
    add_y=0
    direction=""
    snake=[]
    length_snake=1

    ax=round(random.randrange(0,w_screen-snake_size)/10)*10.0
    ay=round(random.randrange(0,h_screen-snake_size)/10)*10.0

    pygame.display.update()

    while not game_over:
        while game_close:
            win.fill(white)
            s="You Lost,score="+str(score)+".Press Q-Quit or R-Restart"
            message(s,red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        play_game()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and direction!="right":
                    add_x=-speed
                    add_y=0
                    direction="left"
                elif event.key==pygame.K_RIGHT and direction!="left":
                    add_x=speed
                    add_y=0
                    direction="right"
                elif event.key==pygame.K_UP and direction!="down":
                    add_x=0
                    add_y=-speed
                    direction="up"
                elif event.key==pygame.K_DOWN and direction!="up":
                    add_x=0
                    add_y=speed
                    direction="down"
        if x>=w_screen or x<0 or y>=h_screen or y<0:
            game_close=True

        x+=add_x
        y+=add_y

        win.fill(black)
        show_score(score,green)
        pygame.display.update()
        pygame.draw.rect(win,red,[ax,ay,snake_size,snake_size])
        pygame.display.update()

        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        if(len(snake)>length_snake):
            snake.remove(snake[0])
        for i in range(len(snake)):
            if i<len(snake)-1:
                if snake[i]==snake_head:
                    game_close=True
            
        for temp in snake:
            pygame.draw.rect(win,blue,[temp[0],temp[1],snake_size,snake_size])
        
        pygame.display.update()

        if x==ax and y==ay:
            score+=1
            ax=round(random.randrange(0,w_screen-snake_size)/10)*10.0
            ay=round(random.randrange(0,h_screen-snake_size)/10)*10.0
            length_snake+=1
        
        clock.tick(speed)
    pygame.quit()

play_game()