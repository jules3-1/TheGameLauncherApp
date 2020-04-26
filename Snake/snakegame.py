import pygame
import random
import time

pygame.init()

BLACK=(0,0,0)
green=(0,200,0)
blue=(0,0,200)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
tan=(210,180,140)
yellow = (255, 255, 102)

disp_width=700
disp_height=500
snake_block=10
size=(disp_width,disp_height)
disp=pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")
gameIcon=pygame.image.load("snakeicon.png")
pygame.display.set_icon(gameIcon)
pygame.display.update()
applepoint=pygame.image.load("apple.jpg")
applepoint=pygame.transform.scale(applepoint,(snake_block,snake_block))
background=pygame.image.load("background.jpg")



clock=pygame.time.Clock()

def text_objects(text, font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def howto():

    howtogo=True

    while howtogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_x:
                     howtogo=False
                     
        BigText = pygame.font.SysFont("comicsansms",60)
        Text = pygame.font.SysFont("comicsansms",20)
        textSurf1, textRect1 = text_objects("How To Play:",BigText,BLACK)
        textRect1.center = ((disp_width/2),(disp_height*0.2))        
        textSurf2, textRect2 = text_objects("1.Press X to Go Back or Quit the Game",Text,BLACK)
        textRect2= (20,(disp_height*0.4))
        textSurf3, textRect3 = text_objects("2.Press G to Go",Text,BLACK)
        textRect3= (20,(disp_height*0.5))
        textSurf4, textRect4 = text_objects("3. Use the arrow Keys to navigate the snake towards the Food",Text,BLACK)
        textRect4= (20,(disp_height*0.6))
        textSurf5, textRect5 = text_objects("4.Press P to Pause",Text,BLACK)
        textRect5= (20,(disp_height*0.7))
        textSurf6, textRect6 = text_objects("5.You will Lose the Game when the snake collides with itself",Text,BLACK)
        textRect6= (20,(disp_height*0.8))
        textSurf7, textRect7 = text_objects("6.The Snake can't change its direction by 180° as it collides with itself",Text,BLACK)
        textRect7= (20,(disp_height*0.9))
        disp.blit(background,[0,0])
        disp.blit(textSurf1, textRect1)
        disp.blit(textSurf2, textRect2)
        disp.blit(textSurf3, textRect3)
        disp.blit(textSurf4, textRect4)
        disp.blit(textSurf5, textRect5)
        disp.blit(textSurf6, textRect6)
        disp.blit(textSurf7, textRect7)
        pygame.display.update()

def scorecard(score):

    scoretext=pygame.font.SysFont("comicsansms",35)
    scoreSurf,scoreRect=text_objects("Your Score: " + str(score),scoretext,yellow)
    scoreRect.center=((disp_width/6),(disp_height/20))
    disp.blit(scoreSurf,scoreRect)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(disp,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(disp, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(disp,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(disp, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg,smallText,BLUE)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    disp.blit(textSurf, textRect)

def our_snake(snake_block, snake_list):
    
    for x in snake_list:
        pygame.draw.rect(disp, BLACK, [x[0], x[1], snake_block, snake_block])


def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText,RED)
    TextRect.center = ((disp_width/2),(disp_height/2))
    disp.blit(TextSurf, TextRect)
    
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

def gameintro():

    intro=True

    while intro:

        disp.fill(BLACK)
        disp.blit(background,[0,-50])
        largeText = pygame.font.SysFont("comicsansms",95)
        TextSurf, TextRect = text_objects("SNAKE 2D", largeText,RED)
        TextRect.center = ((disp_width/2),(disp_height/2))
        disp.blit(TextSurf, TextRect)

        
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

        button("How To Play?",disp_width*0.4,disp_height*0.8,150,50,red,bright_red,howto) 
        
        pygame.display.update()


def gamestart():

    carryOn =True

    x1=disp_width/2
    y1=disp_height/2

    x1_change=0
    y1_change=0

    snake_List = []

    len_snake=1

    foodx = (round(random.randrange(disp_width/10, disp_width*0.9) / 10.0) * 10.0)
    foody = (round(random.randrange(disp_height/10, disp_height*0.9) / 10.0) * 10.0)

    while carryOn:

        disp.fill(BLACK)
        disp.blit(background,[0,-50])
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
                intro=False
                return intro

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_x:
                    carryOn=False
                    intro=False
                    return intro
                if event.key==pygame.K_p:
                    paused()
            elif event.type == pygame.KEYDOWN:
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

        disp.blit(applepoint,(foodx, foody))

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if x1 >= disp_width*0.9:

            x1=disp_width/10

        elif x1 < disp_width/10:

            x1=disp_width*0.9

        elif y1 >= disp_height*0.9:
            
            y1=disp_height/10
            
        elif y1 < disp_height/10:

            y1=disp_height*0.9

                    
        if len(snake_List) > len_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                intro=gameover()
                return intro


        our_snake(snake_block, snake_List)
        scorecard(len_snake-1)
        
        pygame.draw.line(disp,WHITE,[disp_width/10,disp_height*0.1],[disp_width*0.9,disp_height*0.1],5)
        pygame.draw.line(disp,WHITE,[disp_width/10,disp_height*0.9],[disp_width*0.9,disp_height*0.9],5)
        pygame.draw.line(disp,WHITE,[disp_width/10,disp_height*0.1],[disp_width/10,disp_height*0.9],5)
        pygame.draw.line(disp,WHITE,[disp_width*0.9,disp_height*0.1],[disp_width*0.9,disp_height*0.9],5)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = (round(random.randrange(disp_width/10, disp_width*0.9) / 10.0) * 10.0)
            foody = (round(random.randrange(disp_height/10, disp_height*0.9) / 10.0) * 10.0)
            len_snake += 1
            
        clock.tick(20)


def gameover():    

    gameoverText = pygame.font.SysFont("comicsansms",95)
    gTextSurf, gTextRect = text_objects('Game Over', gameoverText,RED)
    gTextRect.center = ((disp_width/2),(disp_height/2))
    disp.blit(gTextSurf, gTextRect)
    pygame.display.update()
    time.sleep(5)
    intro=True
    return intro  
        
gameintro()
quitgame()
