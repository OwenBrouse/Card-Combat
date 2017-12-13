# Game fundimentals
import pygame, sys, math, random
from pygame.locals import *
pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Card Comabat TESTS')

#Background assetes
background = [0,0,0]
backPhoto = pygame.image.load('Card_Choice_Background.png')
backPhoto = pygame.transform.scale(backPhoto,(1000,750))

# Card value storage
cards = []
theChosenCards=[0,0,0,0,0]
cardImage = [pygame.image.load('Card_Standing.png'),pygame.image.load('Card_Punch.png'),pygame.image.load('Card_Kick.png'),pygame.image.load('Card_Dodge.png'),pygame.image.load('Card_Health.png'),pygame.image.load('Card_Front.png'),pygame.image.load('Card_Back.png')]
still = 0

# button value storage
buttons = []
buttonText       = ['Done'       ]
buttonTextColour = [[0  ,0  ,0  ]]
buttonBoxColour  = [[255,255,255]]

playerName = ['player 1' , 'player 2' ]
gameMode = 0

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
        textFont = pygame.font.Font('freesansbold.ttf', 32)
        text = textFont.render(self.text, True, self.textColour)
        textSize = text.get_rect()

        pygame.draw.rect(DISPLAYSURF, self.boxColour,(self.x-(self.width/2),(self.y-(self.heigth/2)),self.width,self.heigth))
        DISPLAYSURF.blit(text,((self.x-(self.width/2))+((self.width-textSize[2])/2),(self.y-(self.heigth/2))+((self.heigth-textSize[3])/2)))

    def clicked(self, xPos, yPos):
        "detects if the mouse cliked plus what button it is"
        if xPos >self.x-(self.width/2) and xPos < (self.x-(self.width/2))+self.width:
            if yPos > self.y-(self.heigth/2) and yPos < (self.y-(self.heigth/2))+self.heigth:
                return self.text

class Card:
    "the object of the cards (size,location,image,movement)"
    def __init__(self, x, y, width, heigth,Id):
        #genaral information
        self.Img = -1
        self.Id = Id
        self.width = width
        self.heigth = heigth
        self.x = x
        self.y = y
        self.selected = False # teleportation

        #Moving infromation
        self.moveByX = 0
        self.moveByY = 0
        self.destX = x
        self.destY = y
        self.speed = 0
        self.computerSelect = False # a slow gliding motion

        #fliping info
        self.flipCount = 0
        self.flipSelect = False # flipping

    def display(self):
        "draws the card"
        image = pygame.transform.scale(cardImage[self.Img], (self.width, self.heigth))

        DISPLAYSURF.blit(image, ((self.x-(self.width/2)),(self.y-(self.heigth/2))))

    def moveTo (self,xx,yy):
        "has the card move closer to a spot"
        self.destX = xx
        self.destY = yy
        self.speed = round(((math.sqrt((self.destX - self.x)**2 + (self.destY - self.y)**2))/50)+1)

        ByX = ((self.destX-self.x))/self.speed
        ByY = ((self.destY-self.y))/self.speed

        self.moveByX = ByX
        self.moveByY = ByY

        self.computerSelect = True

    def goTo (self,mx,my):
        "has the card teleport to a spot"
        self.x = mx
        self.y = my
        
    def getMoving(self):
        "definds the rate witch the card will move at"
        self.x += self.moveByX
        self.y += self.moveByY
        if (round(self.x) == self.destX or round(self.y) == self.destY):
            self.computerSelect = False# just a shortcut for now

    def clicked (self,mX,mY)  :
        "deteminds if the card has been clicked"
        if mY>(self.y-(self.heigth/2)) and mY<(self.y+(self.heigth/2)): 
             if mX >(self.x-(self.width/2)) and mX <(self.x+(self.width/2)):
                return True
                
    def flip (self):
        "visualy filps the card over"
        flipSpeed = 10
        
        if self.flipCount > 999: #unflipping
            self.width += flipSpeed
            self.flipCount -= 1000
            if self.flipCount == 0:
                self.flipSelect = False
                
        elif self.width > flipSpeed: #flip
            self.width -= flipSpeed
            self.flipCount += 1
            
        elif self.width < flipSpeed+1: #is the flip halfway
            self.flipCount *= 1000 
            if self.Img == -1:
                self.Img = self.Id
            else:
                self.Img = -1

                
for numPlayer in range(2):
    gameMode = 0       
    temp = Card(40+(920*numPlayer),65,70,111,-3) #make health/deck card
    cards.append(temp)
    cards[0].Img = cards[0].Id

    temp = Button(850-(700*numPlayer),90,250,55,buttonText[0],buttonTextColour[0],buttonBoxColour[0]) #make button
    buttons.append(temp)

    for new in range (10): #ten random cards
        temp = Card(40+(920*numPlayer),60,70,111,random.randint(1,3))	
        cards.append(temp)
        cards[len(cards)-1].moveTo(275+(((len(cards)-2)%5)*120),300+(((len(cards)-2)//5)*180))


    while gameMode == 0 or still != len(cards)-1:
        
        DISPLAYSURF.blit(backPhoto, (0,-40))    #image
        #DISPLAYSURF.fill((255,175,0))          #a solid colour

        
        for inputNumber in range(5): #draw 5 rectangles
            pygame.draw.rect(DISPLAYSURF, (0,0,0),(80+(90*inputNumber)+(400*numPlayer),0,80,120))

            textFont = pygame.font.Font('freesansbold.ttf', 32)
            text = textFont.render(str(inputNumber+1), True, (255,255,255))
            textSize = text.get_rect()

            DISPLAYSURF.blit(text,((120+(90*inputNumber)+(400*numPlayer))-(textSize[2]/2),60-(textSize[2]/2)))

        for drawButton in range(len(buttons)):
            buttons[drawButton].display()
            
            textFont = pygame.font.Font('freesansbold.ttf', 32)
            text = textFont.render(playerName[numPlayer], True, (255,255,255))
            textSize = text.get_rect()
            
            DISPLAYSURF.blit(text,(850-(700*numPlayer)-(textSize[2]/2),75-(textSize[2]/2)))

       
        still = 0
        for drawCard in range(1,len(cards)):
            if cards[drawCard].computerSelect == True:
                if (round(cards[drawCard].x) != cards[drawCard].destX or round(cards[drawCard].y) != cards[drawCard].destY):
                    cards[drawCard].getMoving()
            if cards[drawCard].flipSelect == True:
                cards[drawCard].flip()
            if cards[drawCard].flipSelect == False and cards[drawCard].selected == False and cards[drawCard].computerSelect == False:
                still += 1 #counts the ammout of cards doing nothing
                
            cards[drawCard].display()
        cards[0].display()

        for event in pygame.event.get():
            if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                for card in range(len(cards)):
                    if cards[card].selected == True:
                          cards[card].goTo(mousex,mousey)
                
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                for card in range(len(cards)):
                    if cards[card].selected == True: #decting if card is in a box
                        for fakeInputNumber in range(5):
                            if mouseY < 120 :
                                if mouseX >(80+(90*fakeInputNumber)+(400*numPlayer)) and mouseX <(160+(90*fakeInputNumber)+(400*numPlayer))and theChosenCards[fakeInputNumber] == 0:
                                    cards[card].goTo((120+(90*fakeInputNumber)+(400*numPlayer)),60)
                                    theChosenCards[fakeInputNumber] = cards[card].Id
                                elif fakeInputNumber == 0: # keep unwanted cards off the bars
                                    cards[card].y = 200
                    cards[card].selected = False #unselect ALL THE CARDS 
                                
                    
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                for card in range(1,len(cards)):
                    if cards[card].clicked(mouseX,mouseY)==True:
                        for fakeInputNumber in range(5): # is this card in a box if so remove it's value
                            if cards[card].x == (120+(90*fakeInputNumber)+(400*numPlayer)) and cards[card].y == 60:
                                theChosenCards[fakeInputNumber] = 0
                        cards[card].selected = True #selects dat card
                        break
                for button in range(len(buttons)):
                    clickedButton = buttons[button].clicked(mouseX,mouseY)
                    if clickedButton == 'Done':
                        print(theChosenCards)
                        gameMode = 1 #move to the next part of the game
                        still = 0
                        for alls in range(1,len(cards)):#move the card into respective piles
                            if cards[alls].y < 65:
                                cards[alls].moveTo(120+(760*numPlayer),65)
                                if cards[alls].Img != -1:
                                    cards[alls].flipSelect = True 
                            else:
                                cards[alls].moveTo(40+(920*numPlayer),65)
                                if cards[alls].Img != -1:
                                    cards[alls].flipSelect = True 
                        
            if event.type == KEYUP:
                for flipAll in range(1,len(cards)):
                    cards[flipAll].flipSelect = True
                        
                            
                        
                
        pygame.display.update()
        fpsClock.tick(FPS)

        
    for kill in range(len(cards)):
        del cards[0]
    for kill in range(len(buttons)):
        del buttons[0]
    theChosenCards=[0,0,0,0,0]
pygame.quit()
sys.exit()
