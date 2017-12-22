#Robert B
#CardCombat
#Version 5.0

import random, sys, pygame, time, math
from pygame.locals import *

pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 700), 0, 32)
pygame.display.set_caption('CardCombat v5.0')

class Fighter:
  "The player class."
  def __init__(self, health, stunned, name, xPos, yPos, stance):
    self.health = health
    self.stunned = stunned
    self.name = name
    self.xPos = xPos
    self.yPos = yPos
    self.stance = stance #What stance the fighter is in (standing, punching, etc.)
    self.stanceName = stances[self.stance]
    self.stanceImg = stanceImgs[self.stance]
  
  def Damage(self, dmg):
    "Damages the player's health by the amount of damage received."
    self.health -= dmg
    
  def Stun(self, stun):
    'Changes the stun status of the recipient.'
    self.stunned = stun
    
  def Display(self, x, y, stance):
    self.xPos = x
    self.yPos = y
    self.stance = stance
    self.stanceName = stances[self.stance]
    self.stanceImg = stanceImgs[self.stance]
    

class Card:
  "The card used in the selection screens."
  def __init__(self, xPos, yPos, isFlipped, atkType, width, height):
    self.xPos = xPos
    self.yPos = yPos
    self.isFlipped = isFlipped
    self.atkType = atkType
    self.backImg = cardImages[0]
    self.frontImg = cardImages[atkType]
    self.img = self.backImg
    self.width = width
    self.height = height
    self.selected = False

    self.compSelect = False

    self.flipCount = 0
    self.flipSelect = False

  def display(self):
        "draws the card"
        image = pygame.transform.scale(cardImage[self.Img], (self.width, self.height))

        DISPLAYSURF.blit(image, ((self.x-(self.width/2)),(self.y-(self.height/2))))

  def clicked(self,mX,mY):
        "Detemines if the card has been clicked"
        if mY>(self.y-(self.height/2)) and mY<(self.y+(self.height/2)): 
             if mX >(self.x-(self.width/2)) and mX <(self.x+(self.width/2)):
                return True

  def flip (self):
        "Visually flips the card over"
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

  def setMove(self, xDest, yDest):
    distX = xDest - self.xPos
    distY = yDest - self.yPos
    incx = distX / 10
    incy = distY / 10
    self.computerSelect = True
    return incx, incy

  def move(self, incX, incY, xDest, yDest):
    if self.xPos != xDest and self.yPos != yDest:
      self.xPos += incX
      self.yPos += incY
    else:
      self.computerSelect = False

  def moveToSetPos(x, y):
    self.xPos = x
    self.yPos = y

    
class DisplayCard:
  "The card that will be displayed in the combat screen."
  def __init__(self,xpos,ypos,width,height,atkType):
    self.xpos = xpos
    self.ypos = ypos
    self.width = width
    self.height = height
    self.atkType = atkType
    self.frontImg = cardImages[0]
    self.backImg = cardImages[1]
    self.img = self.backImg
    self.flipCount = 0
    
  def flip (self):
        "Visually flips the card over"
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
  
class Button:
    "a clickable rectangle plus text"
    def __init__(self, x, y, width, height, text, textColour, boxColour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColour = textColour
        self.boxColour = boxColour
        self.selected = False

    def display(self):
        "shows the button"
        textFont = pygame.font.Font('freesansbold.ttf', 32)
        text = textFont.render(self.text, True, self.textColour)
        textSize = text.get_rect()

        pygame.draw.rect(DISPLAYSURF, self.boxColour,(self.x-(self.width/2),(self.y-(self.height/2)),self.width,self.height))
        DISPLAYSURF.blit(text,((self.x-(self.width/2))+((self.width-textSize[2])/2),(self.y-(self.height/2))+((self.height-textSize[3])/2)))

    def clicked(self, xPos, yPos):
        "detects if the mouse clicked plus what button it is"
        if xPos >self.x-(self.width/2) and xPos < (self.x-(self.width/2))+self.width:
            if yPos > self.y-(self.height/2) and yPos < (self.y-(self.height/2))+self.height:
                return self.text    

#BECAUSE OWEN WANTED IT
intensity = 100

#PLAYERS
p1 = Fighter(20 * intensity, 0, 'Robert', 0, 0, 0)
p2 = Fighter(20 * intensity, 0, 'Owen', 0, 0, 0)

#COMBAT
punchDmg = 1 * intensity
kickDmg = 2 * intensity
flyingKickDmg = 4 * intensity
dmgMult1 = 1
condTurns1 = 0
dmgMult2 = 1
condTurns2 = 0
stanceImgs = [pygame.image.load('Standing.png'),pygame.image.load('Punch.png'),pygame.image.load('Kick.png'),pygame.image.load('Block Kick.png'),pygame.image.load('Taunt.png'),pygame.image.load('Charging.png'),pygame.image.load('Flying Kick.png'),pygame.image.load('Stun.png'),pygame.image.load('Dead.png')]
stances = ['Standing', 'Punch', 'Kick', 'Block Kick', 'Taunt', 'Charging', 'Flying Kick', 'Stunned', 'Dead']

#CARD & CHOICES
choices = [[1,2,3,4,5,6],['Punch','Kick','Block Kick','Taunt','Charging','Flying Kick']]
cardImages = [pygame.image.load('Card_Back.png'),pygame.image.load('Card_Punch.png'),pygame.image.load('Card_Kick.png'),pygame.image.load('Card_Dodge.png'),pygame.image.load('Card_Taunt.png'),pygame.image.load('Card_Charging.png'),pygame.image.load('Card_Flying_Kick.png')]
p1Hand = []
p1Cards = []
p2Hand = []
p2Cards = []
deck1 = [0] * p1.health
for i in range(len(deck1)):
  deck1[i] = random.randint(1, len(choices[0]))
deck2 = [0] * p2.health
for i in range(len(deck2)):
  deck2[i] = random.randint(1, len(choices[0]))
p1MoveCounts = []
p2MoveCounts = []

#TURNS
turns = 5
p1Turns = []
p2Turns = []

#SCREENS
screens = ['menu', 'settings', 'p1cardchoice', 'p2cardchoice', 'game', 'how2play']
screen = 0
fightBackground = pygame.image.load('Fight_Background.png')
cardBackground = pygame.image.load('Card_Choice_Background.png')
background = fightBackground

#BUTTONS
buttons = []
buttonText       = ['Done','Menu','Settings','Game','Tutorial']
buttonTextColour = [[0  ,0  ,0  ]]
buttonBoxColour  = [[255,255,255]]



def Draw(numOfCards, p1H, p2H):
  "Draws a number of cards (depending on their existing hand) to reset each player's hand to 10."
  if p1.health <= 10 and p1.health > 0:
    for i in range(p1.health - len(p1Hand)):
      p1H.append(deck1[0])
      deck1.remove(deck1[0])
  elif p1.health > 10:
    for i in range(numOfCards - len(p1Hand)):
      p1H.append(deck1[0])
      deck1.remove(deck1[0])
  while len(deck1) < p1.health:
    deck1.append(random.randint(1, len(choices[0])))
  
  if p2.health <= 10 and p2.health > 0:
    for i in range(p2.health - len(p2Hand)):
      p2H.append(deck2[0])
      deck2.remove(deck2[0])
  elif p2.health > 10:
    for i in range(numOfCards - len(p2Hand)):
      p2H.append(deck2[0])
      deck2.remove(deck2[0])
  while len(deck2) < p2.health:
    deck2.append(random.randint(1, len(choices[0])))
  return p1H, p2H
  

def Input(numOfTurns, p1H, p2H):
  #Picks the moves.
  p1T = []
  savedHand1 = []
  for x in range(len(p1H)):
    savedHand1.append(p1H[x])
  while len(p1T) != numOfTurns:
    print('\n' + p1.name + ' picks!')
  
    #Displays potential moves.
    for i in range(len(choices[0])):
      print(str(choices[0][i]) + ' = ' + choices[1][i] + ' (' + str(p1MoveCounts[i]) + ')')
    print('\nPick ' + str(numOfTurns) + ' moves.')
    
    #Player input.
    p1T = [int(s) for s in input().split()]  
    if len(p1T) != numOfTurns:
      print('You did not pick five moves.')
    else:
      #Verifies that all cards are in the player's hand, or that the player is holding.
      for i in range(numOfTurns):
        if p1T[i] in p1H:
          print('Move verified!')
          p1H.pop(p1H.index(p1T[i]))
          print(p1H)
        elif p1T[i] == 0:
          print('Move verified!')
          print(p1H)
        else:
          print('Your selected card was not in your hand. Try again.')
          p1T = []
          p1H = savedHand1
          break
  
  #Spacer.
  for i in range(90):
    print('')
  
  #Picks the moves.
  p2T = []
  savedHand2 = []
  for x in range(len(p2H)):
    savedHand2.append(p2H[x])
  while len(p2T) != numOfTurns:
    print('\n' + p2.name + ' picks!')
  
    #Displays potential moves.
    for i in range(len(choices[0])):
      print(str(choices[0][i]) + ' = ' + choices[1][i] + ' (' + str(p2MoveCounts[i]) + ')')
    print('\nPick ' + str(numOfTurns) + ' moves.')
    
    #Player input.
    p2T = [int(s) for s in input().split()]  
    if len(p2T) != numOfTurns:
      print('You did not pick five moves.')
    else:
      for i in range(numOfTurns):
        if p2T[i] in p2H:
          print('Move verified!')
          p2H.pop(p2H.index(p2T[i]))
          print(p2H)
        elif p2T[i] == 0:
          print('Move verified!')
          print(p2H)
        else:
          print('Your selected card was not in your hand. Try again.')
          p2T = []
          p2H = savedHand2
          break
  
  #Spacer.
  for i in range(90):
    print('')

  for card in range(p1T):
    for x in range(p1Cards):
      if card == p1Cards[x].atkType:
        p1Cards.pop(x)
  for card in range(p2T):
    for x in range(p2Cards):
      if card == p2Cards[x].atkType:
        p2Cards.pop(x)
  
  
  return p1T, p2T, p1H, p2H

def Outcomes(c1, c2, cond1, cond2, dmgM1, dmgM2, turn):
  'Calculates the outcome of combat.'
  originHealth1 = p1.health
  originHealth2 = p2.health

  #This section resets any conditional turns.
  if cond1 >= 1:
    cond1 -= 1

  if condTurns1 == 0:
    dmgM1 = 1

  if cond2 >= 1:
    cond2 -= 1

  if cond2 == 0:
    dmgM2 = 1
  
  #If player 1 has chosen to punch (and they are not stunned):
  if c1 == 1 and p1.stunned == 0:
    
    #The game announces that player 1 has thrown a punch. It lands automatically.
    print(p1.name, 'punched', p2.name, end = '!\n')
    
    #If player 2 has chosen to punch (and they are not stunned):
    if c2 == 1 and p2.stunned == 0:
      #The game announces player 2 has thrown a punch. It lands automatically.
      p1.Damage(punchDmg * dmgM2)
      p2.Damage(punchDmg * dmgM1)
      print(p2.name, 'punched', p1.name, end = '!\n')
    
    #Otherwise, if player 2 has chosen to kick (and they are not stunned):
    elif c2 == 2 and p2.stunned == 0:
      #The game announces player 1 has kicked. In this case, it lands automatically and stuns player 1. 
      print(p2.name, 'kicked', p1.name, end = '!\n')
      p1.Damage(kickDmg * dmgM2)
      p2.Damage(punchDmg * dmgM1)
      p1.Stun(1)

    elif c2 == 6 and p2.stunned == 0 and turn > 0:
      if p2Turns[turn - 1] == 5:
        p1.Damage(flyingKickDmg)
        p2.Damage(punchDmg * dmgM1)
        print(p2.name, 'kicked', p1.name, 'from the air!') 
      else:
        print(p2.name, "didn't charge up!")
    
    #For any other moves, player 2 has been hit by a punch. Their stun condition is removed (assuming they have one).  
    else:
      p2.Damage(punchDmg * dmgM1)
      print(p2.name, 'recovered!')
      if c2 == 4 and p2.stunned == 0:
        print(p2.name, 'tried to piss', p1.name, 'off! He/she got punched in the face instead. I guess it worked?')
      elif c2 == 5 and p2.stunned == 0:
        print(p2.name, "couldn't charge their attack!")
        p2Turns[turn] = 0
      p2.Stun(0)
  
  #If player 1 has chosen to kick (and they are not stunned):   
  elif c1 == 2 and p1.stunned == 0:
    print(p1.name, 'kicked', p2.name, end = '!\n')
    
    #If player 2 has chosen to punch (and they are not stunned):
    if c2 == 1 and p2.stunned == 0:
      #The game announces player 2 has been kicked while punching player 1. Player 2 is stunned.
      print(p2.name, 'punched', p1.name, end = '!\n')
      p1.Damage(punchDmg * dmgM2)
      p2.Damage(kickDmg * dmgM1)
      p2.Stun(1)
      
    #If player 2 has chosen to kick (and they are not stunned):  
    elif c2 == 2 and p2.stunned == 0:
      #The game announces both players have been kicked. Both are stunned.
      print(p2.name, 'kicked', p1.name, end = '!\n')
      p1.Damage(kickDmg * dmgM2)
      p2.Damage(kickDmg * dmgM1)
      p1.Stun(1)
      p2.Stun(1)
    
    #If player 2 has chosen to block (and they are not stunned):  
    elif c2 == 3 and p2.stunned == 0:
      #The game announces that player 1's kick has been blocked. Player 1 is now stunned by the block.
      p1.Stun(1)
      print(p2.name, 'blocked!')

    elif c2 == 6 and p2.stunned == 0 and turn > 0:
      if p2Turns[turn - 1] == 5:
        p1.Damage(flyingKickDmg)
        p2.Damage(kickDmg * dmgM1)
        print(p2.name, 'kicked', p1.name, 'from the air!')
      else:
        print(p2.name, "didn't charge up!")  
    else:
      p2.Damage(kickDmg * dmgM1)
      if c2 == 4 and p2.stunned == 0:
        print(p2.name, 'tried to piss', p1.name, 'off! He/she got kicked in the face instead. Well done.')
      elif c2 == 5 and p2.stunned == 0:
        print(p2.name, "couldn't charge their attack!")
        p2Turns[turn] = 0
      p2.Stun(1)
  
  elif c1 == 3 and p1.stunned == 0:
    if c2 == 1 and p2.stunned == 0:
      p1.Damage(punchDmg * dmgM2)
      print(p2.name, 'punched', p1.name, end = '!\n')
      
    elif c2 == 2 and p2.stunned == 0:
      print(p2.name, 'kicked', p1.name, end = '!\n')
      p2.Stun(1)
      print(p1.name, 'blocked!')

    elif c2 == 4 and p2.stunned == 0:
      print(p2.name, 'tried to piss', p1.name, 'off! It worked. For once.')
      dmgM2 = 2
      cond2 = 1

    elif c2 == 5 and p2.stunned == 0:
      print(p2.name, 'is charging up!')
    elif c2 == 6 and p2.stunned == 0 and turn > 0:
      if p2Turns[turn - 1] == 5:
        p2.Stun(1)
        print(p2.name, 'tried to kick', p1.name, 'from the air, but was stopped in their tracks!')
      else:
        print(p2.name, "didn't charge up!")
    else:
      p2.Stun(0)
      
  elif c1 == 4 and p1.stunned == 0:
    if c2 == 1 and p2.stunned == 0:
      print(p2.name, 'punched', p1.name, end = '!\n')
      print(p1.name, 'tried to piss', p2.name, 'off! He/she got punched in the face instead. I guess it worked?')
      p1.Damage(punchDmg * dmgM2)
    elif c2 == 2 and p2.stunned == 0:
      print(p2.name, 'kicked', p1.name, end = '!\n')
      print(p1.name, 'tried to piss', p2.name, 'off! He/she got kicked in the face instead. Well done.')
      p1.Damage(kickDmg * dmgM2)
    elif c2 == 3 and p2.stunned == 0:
      print(p1.name, 'tried to piss', p2.name, 'off! It worked. For once.')
      dmgM2 = 2
      cond2 = 1
    elif c2 == 4 and p2.stunned == 0:
      print(p1.name, 'and', p2.name, 'managed to piss each other off!')
      dmgM1 = 2
      cond1 = 1
      dmgM2 = 2
      cond2 = 1

    elif c2 == 5 and p2.stunned == 0:
      dmgM1 = 2
      cond1 = 1
      print(p2.name, 'is charging up!')
      print(p1.name, 'is pissing', p2.name, 'off!')
    elif c2 == 6 and p2.stunned == 0 and turn > 0:
      if p2Turns[turn - 1] == 5:
        p1.Damage(flyingKickDmg)
        print(p2.name, 'kicked', p1.name, 'from the air!')
        print(p1.name, "couldn't think of a decent insult!")
      else:
        print(p2.name, "didn't charge up!")
    else:
      p2.Stun(0)
      dmgM1 = 2
      cond1 = 1
      print(p2.name, 'recovered!')
      print(p1.name, 'added insult to injury!')

  elif c1 == 5 and p1.stunned == 0:
    if c2 == 1 and p2.stunned == 0:
      p1Turns[turn] = 0
      p1.Damage(punchDmg * dmgM2)
      print(p2.name, 'punched', p1.name, end = '!\n')
      print(p1.name, "couldn't charge up!")
    elif c2 == 2 and p2.stunned == 0:
      p1Turns[turn] = 0
      p1.Damage(kickDmg * dmgM2)
      print(p2.name, 'kicked', p1.name, end = '!\n')
      print(p1.name, "couldn't charge up!")
    else:
      print(p1.name, 'is charging up!')
      if c2 == 4 and p2.stunned == 0:
        cond2 == 1
        dmgM2 == 2
        print(p2.name, 'is pissing', p1.name, 'off!')
      elif c2 == 5 and p2.stunned == 0:
        print('Both fighters are charging up!')
      elif c2 == 6 and p2.stunned == 0 and turn > 0:
        if p2Turns[turn - 1] == 5:
          p1.Damage(flyingKickDmg)
          print(p2.name, 'kicked', p1.name, 'from the air!')
          print(p1.name, "couldn't charge up!")
        else:
          print(p2.name, "didn't charge up!")
      elif p2.stunned == 1:
        p2.Stun(0)
        print(p2.name, 'recovered!')

  elif c1 == 6 and p1.stunned == 0 and turn > 0:
    if p1Turns[turn-1] == 5:
      print(p1.name, 'kicked', p2.name, 'from the air!')
      if c2 != 3:
        p2.Damage(flyingKickDmg)
        if c2 == 1:
          p1.Damage(punchDmg * dmgM2)
          print(p2.name, 'punched', p1.name, '!')
        elif c2 == 2:
          p1.Damage(kickDmg * dmgM2)
          p1.Stun(1)
          print(p2.name, 'kicked', p1.name, '!')
        elif c2 == 4:
          print(p2.name, 'needs better timing...')
        elif c2 == 5:
          p2Turns[turn] = 0
          print(p2.name, "couldn't charge up!")
        elif c2 == 6:
          p1.Damage(flyingKickDmg)
          print('Both fighters kicked in the air!')
      elif c2 == 3:
        p1.Stun(1)
        print(p2.name, 'blocked!')
    else:
      print(p1.name, "didn't charge up!")
  else:
    p1.Stun(0)
    print(p1.name, 'recovered!')
    if c2 == 1 and p2.stunned == 0:
      p1.Damage(punchDmg * dmgM2)
      print(p2.name, 'punched', p1.name, end = '!\n')
    elif c2 == 2 and p2.stunned == 0:
      p1.Damage(kickDmg * dmgM2)
      p1.Stun(1)
      print(p2.name, 'kicked', p1.name, end = '!\n')
    elif c2 == 4 and p2.stunned == 0:
      print(p2.name, 'tried to piss', p1.name, 'off! It worked. For once.')
      dmgM2 = 2
      cond2 = 1
  #Determines what to display after each turn, depending on who has lost health and who was stunned.
  if originHealth1 - p1.health > 0:
    print(p1.name, 'lost', str(originHealth1 - p1.health), 'health!')
  if originHealth2 - p2.health > 0:
    print(p2.name, 'lost', str(originHealth2 - p2.health), 'health!')
  if p1.stunned == 1:
    print(p1.name, 'is stunned!')
  if p2.stunned == 1:
    print(p2.name, 'is stunned!')
  print('')  
  return cond1, cond2, dmgM1, dmgM2

hasDrawn = False
  
while True:  
  DISPLAYSURF.blit(background,(0,0))

  if screen == 0:
    #MainMenu

    hasDrawn = False
    
  elif screen == 1:
    #Settings
    
  elif screen == 2:
    #Player1Choice

    background = cardBackground

    temp = Button(850-(700*numPlayer),90,250,55,buttonText[0],buttonTextColour[0],buttonBoxColour[0]) #make button
    buttons.append(temp)

    for inputNumber in range(5): #draw 5 rectangles
      pygame.draw.rect(DISPLAYSURF, (0,0,0),(80+(90*inputNumber)+(400*numPlayer),0,80,120))
      textFont = pygame.font.Font('freesansbold.ttf', 32)
      text = textFont.render(str(inputNumber+1), True, (255,255,255))
      textSize = text.get_rect()
      DISPLAYSURF.blit(text,((120+(90*inputNumber)+(400*numPlayer))-(textSize[2]/2),60-(textSize[2]/2)))

    deckCard = Card(40,65,0,1,70,111)

    if hasDrawn == False:
      p1Hand, p2Hand = Draw(10, p1Hand, p2Hand)
      hasDrawn = True

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == MOUSEMOTION:
        mousex, mousey = event.pos
        for card in range(len(p1Cards)):
          if p1Cards[card].selected == True:
            p1Cards[card].moveToSetPos(mousex,mousey)

  elif screen == 3:
    #Player2Choice

    background = cardBackground

    temp = Button(850-(700*numPlayer),90,250,55,buttonText[0],buttonTextColour[0],buttonBoxColour[0]) #make button
    buttons.append(temp)
    
    for inputNumber in range(5): #draw 5 rectangles
      pygame.draw.rect(DISPLAYSURF, (0,0,0),(80+(90*inputNumber)+(400*numPlayer),0,80,120))
      textFont = pygame.font.Font('freesansbold.ttf', 32)
      text = textFont.render(str(inputNumber+1), True, (255,255,255))
      textSize = text.get_rect()
      DISPLAYSURF.blit(text,((120+(90*inputNumber)+(400*numPlayer))-(textSize[2]/2),60-(textSize[2]/2)))

    deckCard = Card(960,65,0,1,70,111)

    
    
    for card in range(p1Hand)
    
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == MOUSEMOTION:
        mousex, mousey = event.pos
        for card in range(len(p2Cards)):
          if p2Cards[card].selected == True:
            p2Cards[card].moveToSetPos(mousex,mousey)

  elif screen == 4:
    #GameScreen
    hasDrawn = False
    
  elif screen == 5:
    #HowToPlay
    
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == MOUSEMOTION:
      mousex, mousey = event.pos
      for card in range(len(p2Cards)):
        if p2Cards[card].selected == True:
          p2Cards[card].moveToSetPos(mousex,mousey)
    
  
  pygame.display.update()
  
