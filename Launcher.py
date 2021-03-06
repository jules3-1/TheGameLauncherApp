import os,sys,pygame
pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

initialpath=os.getcwd()

display_width=700
display_height=500
size=(display_width,display_height)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Game Launcher")
background=pygame.image.load("background.jpg").convert()
snakeimage=pygame.image.load("snakeicon.jpg").convert()
airhockeyimage=pygame.image.load("apaddle.jpg").convert()

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
        textSurf1, textRect1 = text_objects("How To Play:",BigText,RED)
        textRect1.center = ((display_width/2),(display_height*0.2))        
        textSurf2, textRect2 = text_objects("1.Press X to Go Back or Quit the Launcher",Text,RED)
        textRect2 = (20,(display_height*0.4))
        textSurf3, textRect3 = text_objects("2.Select your Favourite Game and Click on It when it is highlighted",Text,RED)
        textRect3 = (20,(display_height*0.5))
        screen.blit(background,[0,0])
        screen.blit(textSurf1, textRect1)
        screen.blit(textSurf2, textRect2)
        screen.blit(textSurf3, textRect3)
        pygame.display.update()
    

def openapp(path,file):

    os.chdir(path)
    os.system(file)
    os.chdir(initialpath)


def text_objects(text, font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
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
    

def openinggame(msg,x,y,w,h,ic,ac,path,file,image):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,WHITE,(x-12.5,y-12.5,w+25,h+25))
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1:
            openapp(path,file)         
    else:
        pygame.draw.rect(screen,WHITE,(x-12.5,y-12.5,w+25,h+25))
        pygame.draw.rect(screen, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg,smallText,BLUE)
    textRect.center = ( (x+(w/2)), (y+(h*0.75)) )
    screen.blit(textSurf, textRect)
    screen.blit(image,[x+25,y+10])

def menu():

    intro=True

    while intro:

        Text = pygame.font.SysFont("comicsansms",60)
        textSurf, textRect = text_objects("Game Launcher",Text,RED)
        textRect.center = ((display_width/2),(display_height*0.2))        
        screen.blit(background,[0,0])
        screen.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
            elif event.type==pygame.KEYUP:
                 if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     intro=False


        openinggame("Air Hockey!",display_width*0.2,display_height*0.4,150,150,green,bright_green,'Air Hockey','main.py',airhockeyimage)
        
        openinggame("Snake Game!",display_width*0.6,display_height*0.4,150,150,red,bright_red,"Snake",'snakegame.py',snakeimage)

        button("How To Play?",display_width*0.4,display_height*0.8,150,50,red,bright_red,howto)        

        pygame.display.update()


menu()
pygame.quit()
quit()
