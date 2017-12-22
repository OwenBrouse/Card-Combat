import pygame, sys, math, random
from pygame.locals import *
pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('Card Comabat TITLE SCREEN')
backPhoto = pygame.image.load('Title_Test.png')
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
           
temp = Button(480,350,332,110,"PLAY",[0,0,0],[0,0,0])
buttons.append(temp)
temp = Button(480,580,332,110,"QUIT",[0,0,0],[0,0,0])
buttons.append(temp)


while True:
    

    for allButtons in range(len(buttons)):
        buttons[allButtons].display()

    
    
    for event in pygame.event.get():
        if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
                 
        if event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                        
                for button in range(len(buttons)):
                    clickedButton = buttons[button-1].clicked(mouseX,mouseY)
                    if clickedButton == 'PLAY':
                        print("PLAY")
                        backPhoto = pygame.image.load('Card_Choice_Background.png')
                        backPhoto = pygame.transform.scale(backPhoto,(1000,750))
                        del buttons[0]
                        del buttons[0]
                        #Background assetes
                        background = [0,0,0]
                        backPhoto = pygame.image.load('Card_Choice_Background.png')
                        backPhoto = pygame.transform.scale(backPhoto,(1000,750))

                        # Card value storage
                        cards = []
                        theChosenCards=[0,0,0,0,0]
                        cardImage = [pygame.image.load('Card_Standing.png'),pygame.image.load('Card_Punch.png'),pygame.image.load('Card_Sweep.png'),pygame.image.load('Card_Back.png'),pygame.image.load('Card_Health.png'),pygame.image.load('Card_Front.png'),pygame.image.load('Card_Back2.png')]
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

                                if self.destX != self.x:
                                    self.moveByX = ((self.destX-self.x))/self.speed
                                else:
                                    self.moveByX = 1
                                    self.x -=self.speed
                                    
                                if self.destY != self.y:
                                    self.moveByY = ((self.destY-self.y))/self.speed
                                else:
                                    self.moveByY = 1
                                    self.y -=self.speed

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

                            def clicked (self,mX,mY)  :
                                "deteminds if the card has been clicked"
                                if mY>(self.y-(self.heigth/2)) and mY<(self.y+(self.heigth/2)): 
                                     if mX >(self.x-(self.width/2)) and mX <(self.x+(self.width/2)):
                                        return True
                                        
                            def flip (self):
                                "visualy filps the card over"
                                flipSpeed = 15
                                
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
                                temp = Card(40+(920*numPlayer),60,105,167,random.randint(1,3))	
                                cards.append(temp)
                                cards[len(cards)-1].moveTo(275+(((len(cards)-2)%5)*120),300+(((len(cards)-2)//5)*180))
                        ##    for new in range (30): #ten random cards
                        ##        temp = Card(40+(920*numPlayer),60,70,111,random.randint(1,3))	
                        ##        cards.append(temp)
                        ##        cards[len(cards)-1].moveTo(40+(((len(cards)-2)%10)*100),200+(((len(cards)-2)//10)*200))


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
                backPhoto = pygame.image.load('Fight_Background.png')
                backPhoto = pygame.transform.scale(backPhoto,(1000,750))

                # Card value storage
                cards = []
                theChosenCards=[0,0,0,0,0]
                cardImage = [pygame.image.load('Card_Standing.png'),pygame.image.load('Card_Punch.png'),pygame.image.load('Card_Kick.png'),pygame.image.load('Card_Dodge.png'),pygame.image.load('Card_Heal.png'),pygame.image.load('Card_final (2).png'),pygame.image.load('Card_Flying_Kick.png'),pygame.image.load('Card_Sweep.png'),pygame.image.load('Card_Spin.png'),pygame.image.load('Card_Uppercut.png'),pygame.image.load('Card_Taunt.png'),pygame.image.load('Card_Suicide.png'),pygame.image.load('Card_Stun.png'),pygame.image.load('Card_Prep.png')  ,pygame.image.load('Card_Charging.png'),pygame.image.load('Card_Health.png'),pygame.image.load('Card_Front.png'),pygame.image.load('Card_Back.png')]
                #stand-Punch-kick-dodge-heal-final-flyingkick-sweep-spin-uppercut-taunt-suicide-stun-prep-charge-dead
                #  0      1    2    3     4    5       6        7     8     9      10      11     12  13    14    15  
                personImage = [pygame.image.load('Standing.png')   ,pygame.image.load('Punch.png')     ,pygame.image.load('Kick.png')     ,pygame.image.load('block Kick.png'),pygame.image.load('Heal.png')     ,pygame.image.load('Final_Move.png'),pygame.image.load('Flying Kick.png')     ,pygame.image.load('Sweep.png')     ,pygame.image.load('Spin_Spin.png'),pygame.image.load('Uppercut.png')     ,pygame.image.load('Taunt.png')     ,pygame.image.load('Suicide.png')     ,pygame.image.load('Stun.png')     ,pygame.image.load('Prep_Attack.png'),pygame.image.load('Charging.png')     ,pygame.image.load('Dead.png')       ]                                                                        
                personSize = [[175,350]                            ,[300,400]                          ,[325,500]                         ,[250,475]                          ,[275,475]                         ,[450,363]                          ,[310,310]                                ,[400,300]                          ,[350,400]                         ,[200,500]                             ,[225,420]                          ,[425,500]                            ,[285,400]                         ,[275,500]                           ,[275,300]                             ,[500,175]]


                # button value storage
                buttons = []
                buttonText       = ['Next'       ,'Done'       ]
                buttonTextColour = [[0  ,0  ,0  ],[0  ,0  ,0  ]]
                buttonBoxColour  = [[255,255,255],[255,255,255]]

                playerName = ['player 1' , 'player 2' ]
                gameMode = 1
                count = 0   #Need to be reformated
                tempVar = 0 #Need to be reformated
                tempVar2 = 0#Need to be reformated
                still =0

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
                        self.computerSelect = True
                        
                        self.destX = xx
                        self.destY = yy
                        self.speed = round(((math.sqrt((self.destX - self.x)**2 + (self.destY - self.y)**2))/50)+1)

                        if self.destX != self.x:
                            self.moveByX = ((self.destX-self.x))/self.speed
                        else:
                            self.moveByX = 1
                            self.x -=self.speed
                            
                        if self.destY != self.y:
                            self.moveByY = ((self.destY-self.y))/self.speed
                        else:
                            self.moveByY = 1
                            self.y -=self.speed


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
                def drawPeeps(one,two):
                    
                    if two == 0:
                        DISPLAYSURF.blit(pie2, (500,300))
                    elif two == 4 or two == 6 or two == 3 or two == 9 :  
                        DISPLAYSURF.blit(pie2, (420,200))
                    elif two == 7 or two == 14:  
                        DISPLAYSURF.blit(pie2, (420,400))
                    elif two == 12 or two == 13:  
                        DISPLAYSURF.blit(pie2, (420,270))
                    elif two == 11:  
                        DISPLAYSURF.blit(pie2, (370,270))
                    else:
                        DISPLAYSURF.blit(pie2, (420,300))

                    if one == 4 or one == 6 or one == 3 or one == 9 :  
                        DISPLAYSURF.blit(pie, (300,200))
                    elif one == 7 or one == 14:  
                        DISPLAYSURF.blit(pie, (300,400))
                    elif one == 12 or one == 11 or one == 13:  
                        DISPLAYSURF.blit(pie, (300,270))
                    elif one == 15:  
                        DISPLAYSURF.blit(pie, (100,500))
                    else:
                        DISPLAYSURF.blit(pie, (300,300))

                for numButton in range(1): 
                    temp = Button(500,65,80,100,buttonText[numButton],buttonTextColour[numButton],buttonBoxColour[numButton]) #make health/deck card
                    buttons.append(temp)
                       
                for numPlayer in range(2): 
                    temp = Card(40+(920*numPlayer),65,70,111,-3) #make health/deck card
                    cards.append(temp)
                    cards[numPlayer*6].Img = cards[numPlayer*6].Id
                    for playedCards in range(5):
                        temp = Card(120+(760*numPlayer),65,70,111,random.randint(0,5)) #make health/deck card
                        cards.append(temp)
                        


                while True:
                    if gameMode == 1:#stage 1: deal the cards
                        
                        DISPLAYSURF.blit(backPhoto, (0,-40))    #image
                        #DISPLAYSURF.fill((255,175,0))          #a solid colour

                        still = 0    
                        for drawCard in range(0,len(cards)):
                            cards[drawCard].display()
                            if cards[drawCard].computerSelect == True:
                                if (round(cards[drawCard].x) != cards[drawCard].destX or round(cards[drawCard].y) != cards[drawCard].destY):
                                    cards[drawCard].getMoving()
                            if cards[drawCard].flipSelect == True:
                                cards[drawCard].flip()
                            if cards[drawCard].flipSelect == False and cards[drawCard].computerSelect == False and drawCard != 0 and drawCard != 6:
                                still += 1 #counts the ammout of cards doing nothing
                                

                                
                        if still == len(cards)-2 :
                            if count<5:
                                for numPlayer in range(2): 
                                    cards[(((5-count)*(numPlayer*2))-(5-count))].moveTo(500+((((numPlayer*-2)+1)*(70*count))+(((numPlayer*-2)+1)*75)),65)
                                    #cards[(((5-count)*(numPlayer*2))-(5-count))].flipSelect = True
                                count +=1
                            else:
                                gameMode = 1.5
                                count  =0


                    elif gameMode == 1.5: # stage 2: play the cards              

                        DISPLAYSURF.blit(backPhoto, (0,-40))    #image
                        #DISPLAYSURF.fill((255,175,0))          #a solid colour

                        if still == len(cards) :
                            if count<5:
                                for numPlayer in range(2):
                                    if cards[(((5-count)*(numPlayer*2))-(5-count))].y < 90:
                                        cards[(((5-count)*(numPlayer*2))-(5-count))].moveTo(500+((((numPlayer*-2)+1)*(70*count))+(((numPlayer*-2)+1)*75)),125)
                                        if (((5-count)*(numPlayer*2))-(5-count))>0:
                                            tempVar = cards[(((5-count)*(numPlayer*2))-(5-count))].Id
                                        else:
                                            tempVar2 = cards[(((5-count)*(numPlayer*2))-(5-count))].Id
                                            pygame.time.wait(1000)
                                    else:
                                        if cards[(((5-count)*(numPlayer*2))-(5-count))].Img == -1:
                                            cards[(((5-count)*(numPlayer*2))-(5-count))].flipSelect = True
                                        else:
                                            cards[(((5-count)*(numPlayer*2))-(5-count))].moveTo(500+((((numPlayer*-2)+1)*(70*count))+(((numPlayer*-2)+1)*75)),65)
                                            if  numPlayer == 1: 
                                                pygame.time.wait(1000)
                                                count +=1
                                                tempVar = 0
                                                tempVar2 = 0
                            else:
                                gameMode = 1.75

                        still = 0    
                        for drawCard in range(0,len(cards)):
                            cards[drawCard].display()    
                            if cards[drawCard].flipSelect == False:
                                if cards[drawCard].computerSelect == False:
                                    still += 1 #counts the ammout of cards doing nothing
                                else:
                                    if (round(cards[drawCard].x) != cards[drawCard].destX or round(cards[drawCard].y) != cards[drawCard].destY):
                                        cards[drawCard].getMoving()
                            else:
                                cards[drawCard].flip()


                    elif gameMode == 1.75:#stage 3: waiting for input
                        
                        for drawCard in range(0,len(cards)):
                            cards[drawCard].display()  
                        buttons[0].display()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == MOUSEBUTTONDOWN:
                                mouseX, mouseY = event.pos
                                for button in range(len(cards)):
                                    if buttons[button].clicked(mouseX,mouseY)=='Next':
                                        pygame.quit()
                                        sys.exit()

                    
                    pie = pygame.transform.scale(personImage[tempVar], (personSize[tempVar][0],personSize[tempVar][1]))
                    pie2 = pygame.transform.scale(personImage[tempVar2], (personSize[tempVar2][0],personSize[tempVar2][1]))
                    pie2 = pygame.transform.flip(pie2,True,False)
                    drawPeeps(tempVar,tempVar2)
                        
                    pygame.display.update()
                    fpsClock.tick(FPS)
                    
                    
                for kill in range(len(cards)):
                    del cards[0]
                for kill in range(len(buttons)):
                    del buttons[0]
                theChosenCards=[0,0,0,0,0]



  
                if clickedButton == 'QUIT':
                        pygame.quit()
                        sys.exit()

    DISPLAYSURF.blit(backPhoto, (0,0))
    pygame.display.update()
    fpsClock.tick(FPS)

