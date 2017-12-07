from random import *
 
intensity = 1

numberOfMoves = 5
numberOfPlayers = 2 
deckSize = 20 #health
handSize = 10 #choice

playerList = []
masterDeck = []
odds = []

attack = []
attackDamage = dict()
attackLength = dict()
attackEffect = dict()
#======================================================================================================
#classes===============================================================================================
class Player:
	def __init__(self, moves, hand, masterDeck, name):
		self.name = name
		self.moves = [0]*(moves+1)
		self.target = [0]*(moves)
		self.hand = [0]*(hand)
		self.deck = [0]*(len(masterDeck)-1)
		self.damageMultiplyer = 1
		
		for deckIndex in range(0,len(masterDeck)-1):
			self.deck[deckIndex] = masterDeck[deckIndex]
	
	def info(self):
		"prints the values inside the player"
		print(self.name + ':')
		print("health = deck size = " + str(len(self.deck)))
		print(self.deck)
		print(self.hand)
		print(self.moves)
		print(self.target)
	
	def planMoves(self):
		'deteminds the series of attacks'
		
		#Print++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		print('Yo hand:','\n',self.hand)
		print('key  - ','Atk name','(amount)','(length)','(damage)')
		for attackIndex in range(len(attack)):
			if attack[attackIndex] == 'No attack' or attack[attackIndex] == 'leaveGame':
				print(attackIndex,'  -  ',attack[attackIndex],' ( ∞ ) ',' (',attackLength[attack[attackIndex]],') ',' (',attackDamage[attack[attackIndex]],') ')
			else:	
				print(attackIndex,'  -  ',attack[attackIndex],' (',self.hand.count(attack[attackIndex]),') ',' (',attackLength[attack[attackIndex]],') ',' (',attackDamage[attack[attackIndex]],') ')
		
		#missing turn dection system
		skip = 'FALSE'
		skipList = []
		for turn in range(len((self.moves))-1):
			for turnSkiped in skipList:
				if turn == turnSkiped:
					skip = 'TRUE'
					break
				elif turnSkiped == skipList[len(skipList)-1]:
					skip = 'FALSE'
				
			if skip == 'FALSE':	
		#input++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				choice = 'null'
				while choice == 'null' :
					choice = input(self.name+ ' type your move #' +str(turn+1)+'  -  ')
					
					#interger verification subsection
					for realNumber in range(0,len(attack)):
						if str(realNumber) == choice:
							choice = realNumber
							break
					
			#output+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
					if choice != str(choice):
						if ((attack[choice] in self.hand) or attack[choice] == 'No attack' or attack[choice] == 'leaveGame'):
							
							for futureTurn in range(attackLength[attack[choice]]):
								
								if futureTurn+turn < len(self.moves)-1:
									if futureTurn+1 == attackLength[attack[choice]]:
										self.moves[turn+futureTurn] = attack[choice]
									else:	
										self.moves[turn+futureTurn] = attackEffect[attack[choice]]
									skipList.append(turn+futureTurn)	
							
							if attack[choice] == 'finalMove':
								del self.deck[self.deck.index('finalMove')]
								
							if attack[choice] != 'No attack' and attack[choice] != 'leaveGame':
								self.hand[self.hand.index(attack[choice])] = 'No attack'
						else:	
							choice = 'null'
							print('That card is not in yo hand')
					else:	
						choice = 'null'
						print('That card is not in yo hand')
		print()	
	
	def planTarget(self,others):	
		'determinds the person being attacked for each attack'
		
		
		#Print++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		you = 'null'
		for i in range(numberOfPlayers):
			if others[i].name != self.name:
				print(others[i].name + ' = ' + str(i))
			else:
				you = i
		
		#input++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		for i in range(len(self.target)):
			choice = 'null'
			while choice == 'null':
				choice = input(self.name+ ' type your target for move #' +str(i+1)+'  -  ')
				
				#interger verification subsection
				for j in range(len(others)):
					if str(j) == choice:
						choice = j
						break
				
		#output+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
				if choice != str(choice)  and choice != you:
					self.target[i] = choice
				else:	
					choice = 'null'
					print('try again')
			
	def damage(self,amount):
		'deals damage to the player'
		for i in range(round(amount/intensity)*self.damageMultiplyer):
			if len(self.deck) > 0:
				delete = randint(0,len(self.deck)-1)
				if 	self.deck[delete] != 'finalMove' or len(self.deck)==1:
					del self.deck[delete]
		print(self.name + ' has taken ' +str(amount*self.damageMultiplyer)+' hits')
		
	def makeHand(self):
		preUsed = []
		for handIndex in range(handSize):
			if (len(self.deck)-len(preUsed)) > 0:	
				done = 'FALSE'
				while done == 'FALSE':
					ID = randint(0,len(self.deck)-1)
					if ID not in preUsed:
						if (self.deck[ID] == 'finalMove' and len(self.deck)<10) or self.deck[ID] != 'finalMove':
							self.hand[handIndex] = self.deck[ID]
							preUsed.append(ID)
							done = 'TRUE'
			else:
				self.hand[handIndex] = ''

#======================================================================================================
#funtions==============================================================================================

def setAttacks():
	"defins attacks and give a simple way to turn them off"
	righthook = 'TRUE'
	quickKick = 'TRUE'
	blockKick = 'TRUE'
	twistKick = 'nTRUE'
	megaPunch = 'TRUE'
	speedSpin = 'nTRUE'
	legsSweep = 'nTRUE'
	leaveGame = 'nTRUE'
	fixDamage = 'nTRUE'
	dissTrack = 'TRUE'
	finalMove = 'nTRUE'
	
	
	attack.append('No attack')
	attackDamage['No attack'] = 0*intensity
	attackLength['No attack'] = 1
	attackEffect['No attack'] = 'No attack'
	
	if righthook == 'TRUE':
		attack.append('righthook')
		attackDamage['righthook'] = 1*intensity
		attackLength['righthook'] = 1
		attackEffect['righthook'] = 'charge'
		for i in range(3):
			odds.append('righthook')
	if quickKick == 'TRUE':
		attack.append('quickKick')
		attackDamage['quickKick'] = 2*intensity
		attackLength['quickKick'] = 1
		attackEffect['quickKick'] = 'charge'
		for i in range(3):
			odds.append('quickKick')
	if blockKick == 'TRUE':
		attack.append('blockKick')
		attackDamage['blockKick'] = 0*intensity
		attackLength['blockKick'] = 1
		attackEffect['blockKick'] = 'charge'
		for i in range(3):
			odds.append('blockKick')
	if twistKick == 'TRUE':
		attack.append('twistKick')
		attackDamage['twistKick'] = 11*intensity
		attackLength['twistKick'] = 2
		attackEffect['twistKick'] = 'prep'
		for i in range(1):
			odds.append('twistKick')
	if megaPunch == 'TRUE':
		attack.append('megaPunch')
		attackDamage['megaPunch'] = 9*intensity
		attackLength['megaPunch'] = 5
		attackEffect['megaPunch'] = 'charge'
		for i in range(1):
			odds.append('megaPunch')
	if speedSpin == 'TRUE':
		attack.append('speedSpin')
		attackDamage['speedSpin'] = 3*intensity
		attackLength['speedSpin'] = 5
		attackEffect['speedSpin'] = 'speedSpin'
		for i in range(1):
			odds.append('speedSpin')
	if legsSweep == 'TRUE':
		attack.append('legsSweep')
		attackDamage['legsSweep'] = 1*intensity
		attackLength['legsSweep'] = 1
		attackEffect['legsSweep'] = 'charge'
		for i in range(2):
			odds.append('legsSweep')
	if fixDamage == 'TRUE':
		attack.append('fixDamage')
		attackDamage['fixDamage'] = 2*intensity
		attackLength['fixDamage'] = 2
		attackEffect['fixDamage'] = 'charge'
		for i in range(2):
			odds.append('fixDamage')
	if dissTrack == 'TRUE':
		attack.append('dissTrack')
		attackDamage['dissTrack'] = 0*intensity
		attackLength['dissTrack'] = 1
		attackEffect['dissTrack'] = 'charge'
		for i in range(1):
			odds.append('dissTrack')
	if finalMove == 'TRUE':
		attack.append('finalMove')
		attackDamage['finalMove'] = 5*intensity
		attackLength['finalMove'] = 1
		attackEffect['finalMove'] = 'charge'
			
	if leaveGame == 'TRUE':	
		attack.append('leaveGame')
		attackDamage['leaveGame'] = deckSize*intensity
		attackLength['leaveGame'] = numberOfMoves
		attackEffect['leaveGame'] = 'leaveGame'
	
	#print(attack)
	#print(attackDamage)
	#print(attackLength)
	#print(attackEffect)
	
def checkValues():
	"Checks for game breaking inputs"
	if deckSize>=handSize and handSize>=numberOfMoves:	
		if numberOfPlayers > 1 and numberOfMoves > 1 and intensity > 0:
			for damage in attack:
				if attackDamage[damage] <= 0 and damage != 'blockKick' and damage != 'No attack'and damage != 'legsSweep' and damage != 'dissTrack':
					return 'FAlSE'
				else:
					if damage == attack[len(attack)-1]:
						return 'TRUE'
		else:
			return 'FLASE'
	else:
		return 'FLASE'		
		
def battle(what,who,when,person):
	"detiminds the out come of the attacks"
	#if you don't understand the variables :
		#what		=	the attack bieing performed
		#who		=	what player is being attacked
		#when		=	what round/section of a list that is currently happening 
		#person	=	what player is doinf the attack
	if what == 'No attack':
		weird = randint(1, 50) 
		if weird == 1:
			print(playerList[person].name + ' is waiting')
		elif weird == 2:
			print(playerList[person].name + ' is taking a nap')
		elif weird == 3:
			print(playerList[person].name + ' is just chillin')
		elif weird == 4:
			print(playerList[person].name + ' is pondering the meaning of life')
		elif weird == 5:
			print(playerList[person].name + ' is not feeling it')
		elif weird == 6:
			print(playerList[person].name + ' is having an off day')
		elif weird == 7:
			print(playerList[person].name + ' is taking a well earned break')
		elif weird == 8:
			print(playerList[person].name + ' is taking a breather')
		elif weird == 9:
			print(playerList[person].name + ' is holding back')
		elif weird == 10:
			print(playerList[person].name + ' is playing some b-ball outside the school')
		elif weird == 11:
			print(playerList[person].name + ' is going vegan')
		elif weird == 12:
			print(playerList[person].name + ' is having a me-day')
		elif weird == 13:
			print(playerList[person].name + ' is looking at themself in the mirror')
		elif weird == 14:
			print(playerList[person].name + ' is checking their phone')
		elif weird == 15:
			print(playerList[person].name + ' is AFK')
		elif weird == 16:
			print(playerList[person].name + ' is out for a pee')
		elif weird == 17:
			print(playerList[person].name + ' is out to lunch')
		elif weird == 18:
			print(playerList[person].name + ' is taking a selfie')
		elif weird == 19:
			print(playerList[person].name + ' is in the upside down')
		elif weird == 20:
			print(playerList[person].name + ' is eating some schezwan sauce')
		elif weird == 21:
			print(playerList[person].name + ' is buffering')
		elif weird == 22:
			print(playerList[person].name + ' has high ping')
		elif weird == 23:
			print(playerList[person].name + ' is installing 1 of 29353 updates')
		elif weird == 24:
			print(playerList[person].name + ' has lost connection')
		elif weird == 25:
			print(playerList[person].name + ' is under the weather')
		else:
			print(playerList[person].name + ' is not attacking')
	elif what == 'prep':
		print(playerList[person].name + ' is preparing for an attack')
	elif what == 'stun':
		print(playerList[person].name +' is stunned')
	elif what == 'charge':
		print(playerList[person].name +' is charging up an attack')
	elif what == 'righthook':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'speedSpin':
					for screwed in range(len(playerList[who].moves)-1):	
						playerList[who].moves[screwed] = 'stun'
			elif playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'dissTrack':
				playerList[playerList[who].target[when]].damageMultiplyer = 1
				print(playerList[who].name + ' has gotten their face caved in instead of throwing shade')
	elif what == 'quickKick':
		print(playerList[person].name + ' ' + what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == 'blockKick' and playerList[who].target[when] == person:
			print('but ' + playerList[who].name + ' blocks it')
			playerList[person].moves[when+1] = 'stun'
			print(playerList[person].name + ' is now stunned')
		elif playerList[who].moves[when] == what:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'speedSpin':
					for screwed in range(len(playerList[who].moves)-1):	
						playerList[who].moves[screwed] = 'stun'
			elif playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'dissTrack':
				playerList[playerList[who].target[when]].damageMultiplyer = 1
				print(playerList[who].name + ' has gotten kick in the nut instead of throwing shade')
	elif what == 'blockKick':
		print(playerList[person].name + ' is blocking')
	elif what == 'twistKick':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		elif playerList[who].moves[when] == 'blockKick' and playerList[who].target[when] == person:
			print('but ' + playerList[who].name + ' blocks it')
			playerList[person].moves[when+1] = 'stun'
			print(playerList[person].name + ' is now stunned')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'speedSpin':
					for screwed in range(len(playerList[who].moves)-1):	
						playerList[who].moves[screwed] = 'stun'
			elif playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'dissTrack':
				playerList[playerList[who].target[when]].damageMultiplyer = 1
				print(playerList[who].name + ' has gotten kick across the room instead of throwing shade')
	elif what == 'megaPunch':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'speedSpin':
				for screwed in range(len(playerList[who].moves)-1):	
					playerList[who].moves[screwed] = 'stun'
			elif playerList[who].moves[when] == 'dissTrack':
				playerList[playerList[who].target[when]].damageMultiplyer = 1
				print(playerList[who].name + ' has learned how to fly instead of throwing shade')
	elif what == 'speedSpin':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'dissTrack':
				playerList[playerList[who].target[when]].damageMultiplyer = 1
				print(playerList[who].name + ' has gotten smacked arcoss the face instead of throwing shade')
	elif what == 'legsSweep':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].moves[when+1] = 'stun'
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'speedSpin':
				for screwed in range(len(playerList[who].moves)-1):	
					playerList[who].moves[screwed] = 'stun'
	elif what == 'leaveGame':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[person].name)
		playerList[person].damage(attackDamage[what])
	elif what == 'fixDamage':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[person].name)
		for heals in range(attackDamage[what]):
			cardType = randint(1,len(attack)-1)
			playerList[person].deck.append(attack[cardType])
	elif what == 'finalMove':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'speedSpin':
					for screwed in range(len(playerList[who].moves)-1):	
						playerList[who].moves[screwed] = 'stun'
			elif playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
			elif playerList[who].moves[when] == 'dissTrack':
				playerList[playerList[who].target[when]].damageMultiplyer = 1
				print(playerList[who].name + ' has gotten finalized instead of throwing shade')
	elif what == 'dissTrack':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damageMultiplyer = 2
	elif what != 'dissTrack':
			playerList[who].damageMultiplyer = 1
	else:
		print('value error')

def clear(numLines):
	'prints empty lines to flood the screen'
	for helloRobertYouDontNeedToReadThisItsAnEasterEgg in range(numLines):
		print()
		
def makeDeck():
	for cardNumber in range(deckSize+1):
		if attack.count('finalMove') > 0 and masterDeck.count('finalMove') == 0:
			masterDeck.append('finalMove')
		else:	
			cardType = randint(0,len(odds)-1)
			masterDeck.append(odds[cardType])
#======================================================================================================
#run===================================================================================================


#setup-------------------------------------------------------------------------------------------------
setAttacks()
makeDeck()
if checkValues()=='TRUE':
	clear(50)
	for players in range(numberOfPlayers):
		temp = Player(numberOfMoves,handSize,masterDeck,str(input('player '+ str(players+1) +' whats your name - ')))	
		playerList.append(temp)
	
	#input-------------------------------------------------------------------------------------------------
	while len(playerList[0].deck)>0 and len(playerList[1].deck)>0:
		clear(50)
		for player in range(len(playerList)):
			playerList[player].makeHand()
			#playerList[player].info()			
			playerList[player].planMoves()
		
			if numberOfPlayers > 2:
				playerList[player].planTarget(playerList)
			else:
				playerList[1].target = [0]*numberOfMoves
				playerList[0].target = [1]*numberOfMoves
			clear(100)
			
		
	#run---------------------------------------------------------------------------------------------------
		for number in range(numberOfMoves):
			print('round ' + str(number+1)+' ------------------')
			for player in range(numberOfPlayers):
				battle(playerList[player].moves[number], playerList[player].target[number],number,player)
				#playerList[player].info()
				print()
			
	#outup-------------------------------------------------------------------------------------------------
		for players in range(numberOfPlayers):
			print(playerList[players].name + ' is at '+ str((len(playerList[players].deck))*intensity))
		input('press enter to continue')
	
	#end+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	for players in range(numberOfPlayers):
		print(playerList[players].name, len(playerList[players].deck),sep=(' - '),end=('.....................'+"\n"))	
	for players in range(numberOfPlayers):
		if len(playerList[players].deck) == 0:
			print(playerList[players].name + 'loses')
else:
	print('Some values in your game are corrupted')
