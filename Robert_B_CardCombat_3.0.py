#Robert B
#CardCombat
#Version 3.0

import random

class Fighter:
  def __init__(self, health, stunned, name, xPos, yPos, stance):
    self.health = health
    self.stunned = stunned
    self.name = name
    self.xPos = xPos
    self.yPos = yPos
    self.stance = stance
  
  def Damage(self, dmg):
    'Damages the recipient.'
    self.health -= dmg
    
  def Stun(self, stun):
    'Changes the stun status of the recipient.'
    self.stunned = stun
    
  def Display(self, x, y, stance):
    self.xPos = x
    self.yPos = y
    self.stance = stance

p1 = Fighter(20, 0, str(input("Enter Player 1's Name:")), 0, 0, 0)
p2 = Fighter(20, 0, str(input("Enter Player 2's Name:")), 0, 0, 0)
punchDmg = 1
kickDmg = 2
dmgMult1 = 1
condTurns1 = 0
dmgMult2 = 1
condTurns2 = 0
choices = [[1,2,3,4],['Punch','Kick','Block Kick','Taunt']]
turns = 5
p1Turns = []
p2Turns = []
p1Hand = []
p2Hand = []
p1MoveCounts = []
p2MoveCounts = []

def Draw(numOfCards, p1H, p2H):
  "Draws a number of cards (depending on their existing hand) to reset each player's hand to 10."
  for i in range(numOfCards - len(p1Hand)):
    p1H.append(random.randint(1,4))
  for i in range(numOfCards - len(p2Hand)):
    p2H.append(random.randint(1,4))
      
  #Sorts each hand for easier management.
  p1H.sort()
  p2H.sort()
  
  #Collects the amount of choices the player has into lists.
  p1M = []
  p2M = []
  for i in range(1,len(choices[0]) + 1):
    p1M.append(p1H.count(i))
    p2M.append(p2H.count(i))
  return p1M, p2M, p1H, p2H
  

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
        else:
          print('Your selected card was not in your hand. Try again.')
          p2T = []
          p2H = savedHand2
          break
  
  #Spacer.
  for i in range(90):
    print('')
  
  return p1T, p2T, p1H, p2H

def Outcomes(c1, c2, cond1, cond2, dmgM1, dmgM2):
  'Calculates the outcome of combat.'
  originHealth1 = p1.health
  originHealth2 = p2.health
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
    
    #For any other moves, player 2 has been hit by a punch. Their stun condition is removed (assuming they have one).  
    else:
      p2.Damage(punchDmg * dmgM1)
      print(p2.name, 'recovered!')
      if c2 == 4 and p2.stunned == 0:
        print(p2.name, 'tried to piss', p1.name, 'off! They got punched in the face instead. I guess it worked?')
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
      
    else:
      p2.Damage(kickDmg * dmgM1)
      if c2 == 4 and p2.stunned == 0:
        print(p2.name, 'tried to piss', p1.name, 'off! They got kicked in the face instead. Well done.')
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
    else:
      p2.Stun(0)
      print(p2.name, 'recovered!')
      
  elif c1 == 4 and p1.stunned == 0:
    if c2 == 1 and p2.stunned == 0:
      print(p2.name, 'punched', p1.name, end = '!\n')
      print(p1.name, 'tried to piss', p2.name, 'off! They got punched in the face instead. I guess it worked?')
      p1.Damage(punchDmg * dmgM2)
    elif c2 == 2 and p2.stunned == 0:
      print(p2.name, 'kicked', p1.name, end = '!\n')
      print(p1.name, 'tried to piss', p2.name, 'off! They got kicked in the face instead. Well done.')
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
    else:
      p2.Stun(0)
      print(p2.name, 'recovered!')
      print(p1.name, 'added insult to injury!')
  elif p1.stunned == 1:
    p1.Stun(0)
    print(p1.name, 'recovered!')
    if c2 == 1 and p2.stunned == 0:
      p1.Damage(punchDmg * dmgM2)
      print(p2.name, 'punched', p1.name, end = '!\n')
    elif c2 == 2 and p2.stunned == 0:
      p1.Damage(kickDmg * dmgM2)
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
  
while p1.health > 0 and p2.health > 0:
  p1MoveCounts, p2MoveCounts, p1Hand, p2Hand = Draw(10, p1Hand, p2Hand)
  p1Turns, p2Turns, p1Hand, p2Hand = Input(turns, p1Hand, p2Hand)
  for i in range(turns):
    condTurns1, condTurns2, dmgMult1, dmgMult2 = Outcomes(p1Turns[i], p2Turns[i], condTurns1, condTurns2, dmgMult1, dmgMult2)
    if p1.health == 0 or p2.health == 0:
      break
  print(p1.name, 'health:', str(p1.health))
  print(p2.name, 'health:', str(p2.health))
if p1.health == 0 and p2.health == 0:
  print('Draw!')
elif p2.health == 0:
  print(p1.name, 'wins!')
else:
  print(p2.name, 'wins!')

