# Import the pygame library and initialise the game engine
import pygame
pygame.init()
from paddle import Paddle
from ball import Ball
import time
import random
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
grey=(220,220,220)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

display_width=700
display_height=500
winscore=3#the score needed to win
clock = pygame.time.Clock()

# Open a new window
size = (display_width,display_height)#size of window
screen = pygame.display.set_mode(size)#setting the size of window
pygame.display.set_caption("Air Hockey 2D")#updating the heading
gameIcon=pygame.image.load('apaddle.jpg')#icon image
pygame.display.set_icon(gameIcon)#setting the icon
background=pygame.image.load("background.jpg").convert()

    
paddleA = Paddle(BLUE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(GREEN, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball=Ball(RED,10,10)
ball.rect.x=345
ball.rect.y=195

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
    
# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


def text_objects(text, font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg,smallText,BLUE)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def gameintro():

    intro=True

    while intro:

        screen.fill(BLACK)
        screen.blit(background,[-6.5,0])
        largeText = pygame.font.SysFont("comicsansms",95)
        TextSurf, TextRect = text_objects("Air Hockey", largeText,RED)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
            elif event.type==pygame.KEYUP:
                 if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     intro=False
                 if event.key==pygame.K_g:
                     intro=gamestart()


        button("GO!",150,350,100,50,green,bright_green,gamestart)
        
        button("Quit!",450,350,100,50,red,bright_red,quitgame)

        pygame.display.update()


def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText,RED)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    
    global pause
    pause=True
    
    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYUP:                
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    quitgame()
                if event.key==pygame.K_p:
                    unpause()      

        button("Continue",150,350,100,50,green,bright_green,unpause)
        button("Quit",450,350,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():

    global pause
    pause=False


def quitgame():

    pygame.quit()
    quit()
    

def scoreboard(score,side,color):

    scoreAtext = pygame.font.SysFont("comicsansms",50)
    ATextSurf, ATextRect = text_objects(score,scoreAtext,color)
    ATextRect.center = ((side),(display_height/10))
    screen.blit(ATextSurf,ATextRect)
       
        
def gamestart():
    
    carryOn=True
    clock=pygame.time.Clock()

    scoreA=0
    scoreB=0
    while carryOn:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
                intro=False
                return intro
            elif event.type==pygame.KEYUP:                
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    carryOn=False
                    intro=True
                    return intro
                if event.key==pygame.K_p:
                    paused()

                     
        #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveup(5)
        if keys[pygame.K_s]:
            paddleA.movedown(5)
        if keys[pygame.K_UP]:
            paddleB.moveup(5)
        if keys[pygame.K_DOWN]:
            paddleB.movedown(5)  

        all_sprites_list.update()

        if ball.rect.x>=690:
            if (150<ball.rect.y<350):
                scoreA+=1
                ball.rect.x=40
                ball.rect.y=200
                ball.velocity=[random.randint(6,12),random.randint(-8,8)]
                time.sleep(1)
            else:
                ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            if (150<ball.rect.y<350):
                scoreB+=1
                ball.rect.x=650
                ball.rect.y=200
                ball.velocity=[random.randint(-12,-6),random.randint(-8,8)]
                time.sleep(1)
            else:
                ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
            ball.bounce()
            
        screen.fill(BLACK)    
        screen.blit(background,[-6.5,0])#fills the screen with background
        
        #draws the line
        pygame.draw.line(screen, RED, [700, 150], [695,150],2)
        pygame.draw.line(screen, RED, [700,350], [695,350],2)
        pygame.draw.line(screen, RED, [695,150], [695,350],2)
        pygame.draw.line(screen, RED, [0, 150], [5,150],2)
        pygame.draw.line(screen, RED, [0,350], [5,350],2)
        pygame.draw.line(screen, RED, [5,150], [5,350],2)
        #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        scoreboard(str(scoreA),(display_width/3),BLUE)
        scoreboard(str(scoreB),(2*(display_width/3)),GREEN)

        pygame.display.flip()#updates all the changes into the window

        if scoreA>=winscore:
            
            intro=winner("Team A Wins",BLUE)
            return intro
        
        if scoreB>=winscore:
            
            intro=winner("Team B Wins",GREEN)
            return intro

        clock.tick(60)#limit to 60fps

def winner(teamname,color):    

    winnerText = pygame.font.SysFont("comicsansms",95)
    WTextSurf, WTextRect = text_objects(teamname, winnerText,color)
    WTextRect.center = ((display_width/2),(display_height/2))
    screen.blit(WTextSurf, WTextRect)
    pygame.display.update()
    time.sleep(5)
    intro=True
    return intro    



gameintro()
pygame.quit()
quit()

