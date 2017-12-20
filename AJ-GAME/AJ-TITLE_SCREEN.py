import pygame, sys, math, random
from pygame.locals import *
pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Card Comabat TITLE SCREEN')
backPhoto = pygame.image.load('Card_Choice_Background.png')
backPhoto = pygame.transform.scale(backPhoto,(1000,750))
buttons = []
class Button:
    "a clickable rectangle plus text"
    def __init__(self, x, y, width, heigth, text, textColour, boxColour):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.text = text
        self.textColour = textColour
        self.boxColour = boxColour
        self.selected = False

    def display(self):
        "showes the button"
        textFont = pygame.font.Font('BlackDahlia-kerned.ttf', 70)
        text = textFont.render(self.text, True, self.textColour)
        textSize = text.get_rect()

        pygame.draw.rect(DISPLAYSURF, self.boxColour,(self.x-(self.width/2),(self.y-(self.heigth/2)),self.width,self.heigth))
        DISPLAYSURF.blit(text,((self.x-(self.width/2))+((self.width-textSize[2])/2),(self.y-(self.heigth/2))+((self.heigth-textSize[3])/2)))

    def clicked(self, xPos, yPos):
        "detects if the mouse cliked plus what button it is"
        if xPos >self.x-(self.width/2) and xPos < (self.x-(self.width/2))+self.width:
            if yPos > self.y-(self.heigth/2) and yPos < (self.y-(self.heigth/2))+self.heigth:
                return self.text
           
temp = Button(500,350,200,75,"PENIS",[0,0,0],[255,255,0])
buttons.append(temp)
temp = Button(500,450,200,75,"ASS",[0,255,0],[255,0,255])
buttons.append(temp)
temp = Button(500,550,650,75,"BLACK DAHLIA MURDER",[255,0,0],[255,255,255])
buttons.append(temp)


while True:
    DISPLAYSURF.blit(backPhoto, (0,-40))

    for allButtons in range(len(buttons)):
        buttons[allButtons].display()

    
    
    for event in pygame.event.get():
            if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
                 
            if event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                        
                for button in range(len(buttons)):
                    clickedButton = buttons[button].clicked(mouseX,mouseY)
                    if clickedButton == 'PENIS':
                        del buttons[0]
                    if clickedButton == 'ASS':
                        del buttons[1]
                    if clickedButton == 'BLACK DAHLIA MURDER':
                        del buttons[2]
                                
    pygame.display.update()
    fpsClock.tick(FPS)

