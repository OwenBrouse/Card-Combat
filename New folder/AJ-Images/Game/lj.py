# Game fundimentals
import pygame, sys, math, random
from pygame.locals import *
pygame.init()
FPS = 60 
fpsClock = pygame.time.Clock()

#Background assetes
background = [0,0,0]
backPhoto = pygame.image.load('Card_Choice_Background.png')
backPhoto = pygame.transform.scale(backPhoto,(1000,750))

# Card value storage
cards = []
theChosenCards=[0,0,0,0,0]
cardImage = [pygame.image.load('Card_Standing.png'),pygame.image.load('Card_Punch.png'),pygame.image.load('Card_Kick.png'),pygame.image.load('Card_Dodge.png'),pygame.image.load('Card_Health.png'),pygame.image.load('Card_Front.png'),pygame.image.load('Card_Back.png')]

# button value storage
buttons = []
buttonText       = ['Done'       ]
buttonTextColour = [[0  ,0  ,0  ]]
buttonBoxColour  = [[255,255,255]]


DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Card Comabat TESTS')

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
                if self.text == 'Done':
                    print(theChosenCards)
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
            self.computerSelect = False
            self.flipSelect = True # just a shortcut for now

    def clicked (self,mX,mY)  :
        "deteminds if the card has been clicked"
        if mY>(self.y-(self.heigth/2)) and mY<(self.y+(self.heigth/2)): 
             if mX >(self.x-(self.width/2)) and mX <(self.x+(self.width/2)):
                return True
                
    def flip (self):
        "visualy filps the card over"
        flipSpeed = 4
        
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


##for numberOfCard in range(78):        
##    temp = Card(400,400,70,111)	
##    cards.append(temp)
##for numberOfCard in range(len(cards)):        
##    cards[numberOfCard].moveTo((77*(numberOfCard%13))+38,(116*(numberOfCard//13))+57)	
       
temp = Card(40,60,70,111,-3) #make health/deck card
cards.append(temp)
cards[0].Img = cards[0].Id

temp = Button(850,65,250,75,buttonText[0],buttonTextColour[0],buttonBoxColour[0]) #make button
buttons.append(temp)

for new in range (10): #ten random cards
    temp = Card(40,60,70,111,random.randint(1,3))	
    cards.append(temp)
    cards[len(cards)-1].moveTo(275+(((len(cards)-2)%5)*120),300+(((len(cards)-2)//5)*180))


while True:
    
    DISPLAYSURF.blit(backPhoto, (0,-50))    #image
    #DISPLAYSURF.fill((255,175,0))          #a solid colour

    
    for inputNumber in range(5): #draw 5 rectangles
        pygame.draw.rect(DISPLAYSURF, (0,0,0),(80+(90*inputNumber),0,80,120))

        textFont = pygame.font.Font('freesansbold.ttf', 32)
        text = textFont.render(str(inputNumber+1), True, (255,255,255))
        textSize = text.get_rect()

        DISPLAYSURF.blit(text,((120+(90*inputNumber))-(textSize[2]/2),60-(textSize[2]/2)))

    for drawButton in range(len(buttons)):
        buttons[drawButton].display()
   
    for drawCard in range(len(cards)):
        if cards[drawCard].computerSelect == True:
            if (round(cards[drawCard].x) != cards[drawCard].destX or round(cards[drawCard].y) != cards[drawCard].destY):
                cards[drawCard].getMoving()
        if cards[drawCard].flipSelect == True:
            cards[drawCard].flip()

        cards[drawCard].display()


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
                        if mouseX >(80+(90*fakeInputNumber)) and mouseX <(160+(90*fakeInputNumber))and mouseY < 120 and theChosenCards[fakeInputNumber] == 0:
                            cards[card].goTo(120+(90*fakeInputNumber),60)
                            theChosenCards[fakeInputNumber] = cards[card].Id
                cards[card].selected = False #unselect ALL THE CARDS WHAAAAAHAAAAHAAAAAAAAAAAAAAA
                            
                
        elif event.type == MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            for card in range(1,len(cards)):
                if cards[card].clicked(mouseX,mouseY)==True:
                    for fakeInputNumber in range(5): # is this card in a box if so remove it's value
                        if cards[card].x == 120+(90*fakeInputNumber) and cards[card].y == 60:
                            theChosenCards[fakeInputNumber] = 0
                    cards[card].selected = True #selects dat card
                    break
            for button in range(len(buttons)):
                buttons[button].clicked(mouseX,mouseY)
                    
##        elif event.type == KEYUP:
                    
                        
                    
            
    pygame.display.update()
    fpsClock.tick(FPS)
