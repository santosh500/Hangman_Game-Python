import pygame, sys
import time
from pygame.locals import *
pygame.init()


white=(255,255,255)
black=(0,0,0)
magenta=(238,0,238)
blue=(0,0,255)
red=(255,0,0)
words=[]
numbers=[]
numbers3=[]
size=0
global food
food=0
global mark
mark=0
#global name=""
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('hangman')


def openingscreen():

    screen1=True

    while screen1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    screen1=False
                if event.key==pygame.K_DOWN:
                    pygame.quit()
                    sys.exit()
                    
        gameDisplay.fill(white)
        title="Hangman Game"
        title2="by Santosh Charles"
        sys_font=pygame.font.SysFont("None", 60)
        render2=sys_font.render(title,0,red)
        gameDisplay.blit(render2, (180, 100))
        sys_font=pygame.font.SysFont("None", 60)
        render2=sys_font.render(title2,0,red)
        gameDisplay.blit(render2, (180, 150))
        pygame.display.update()

    #time.sleep(5)
        
    
def player1():
    gameDisplay.fill(blue)
    global name
    name=""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: #clicked on x sign
                pygame.quit()
                sys.exit()
            sys_font = pygame.font.SysFont("None", 60)
            rendered = sys_font.render('Word please', 0, magenta)
            gameDisplay.blit(rendered, (180,100)) #gameDisplay is screen and blit is to do it quick and do it 180 and down 100
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                    words.append(event.unicode)
                    numbers.append(0)
                    numbers3.append(0)
                elif event.unicode.isdigit():
                    return
            rd1=sys_font.render('Cows are cool',0,magenta)
            rd2=sys_font.render(name,0, magenta)
            gameDisplay.blit(rd2, (180,170))
            pygame.display.update()
            
def maingame():
    screen2=True

    while screen2:
        experiment1()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.unicode.isdigit():
                    return
                elif event.unicode.isalpha():
                    i=0
                    for items in words:
                        if(items==event.unicode):
                            print("hi")
                            numbers[i]=1
                        i+=1
                tallymarks()  
        print(food)
        pygame.display.update()
        
def printList():
    for item in words:
        print(item, end=" ")
    for item1 in numbers:
        print(item1, end=" ")


def printList2():
    for item in numbers:
        print(item, end=" ")
    for item1 in numbers3:
        print(item1, end=" ")

def drawspaces():
    o=0
    size=len(numbers)
    x=35
    while o < size:
        pygame.draw.rect(gameDisplay, black, [x,500,50,10])
        o+=1
        x+=60

def experiment1():
        global food
        gameDisplay.fill(white)
        o=0
        size=len(numbers)
        x=35
        y=500

        #drawhangman()
        if(food==1):
            pygame.draw.circle(gameDisplay,black,[100,100],40)
            pygame.draw.rect(gameDisplay, black, [200,300,50,50])
        elif(food==2):
            pygame.draw.rect(gameDisplay, black, [100,200, 50, 68])
            pygame.draw.rect(gameDisplay, black, [200,300,50,50])
            
            
        while o < size:
            if(numbers[o]==0):
                pygame.draw.rect(gameDisplay, black, [x,500,50,10])
            elif(numbers[o]==1):
                cars=words[o]
                sys_font = pygame.font.SysFont("None", 45)
                rendered5 = sys_font.render(cars, 0, red)
                gameDisplay.blit(rendered5, (x,y))
            o+=1
            x+=60

def tallymarks():
    global food
    global mark
    i=0
    for items in numbers:
        if(items != numbers3[i]):
            mark=1
            break
        else:
            mark=2
        i+=1
    g=0
    for items2 in numbers:
        numbers3[g]=items2
        g += 1
    while(mark==2):
        i=0
        food+=1
        break
        


    #drawhangman(james)

    
def drawhangman(tacos):
    if(mark==1):
        i=0
        while(i<1):
            print("cows")
            tacos+=1
            i+=1

def printWord():
    print(name)
    pygame.quit()
    sys.exit()

openingscreen()
player1()


maingame()
printList()
printWord()
