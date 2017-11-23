from random import *
 
intensity = 5000
totalHealth = 20*intensity
numberOfPlayers = 2
numberOfMoves = 5
playerList = []

attack = []
attackDamage = dict()
attackLength = dict()
#======================================================================================================
#classes===============================================================================================
class Player:
	def __init__(self, moves, health, name):
		self.health = health
		self.name = name
		self.moves = [0]*(moves+1)
		self.target = [0]*(moves)

	def info(self):
		"prints the values inside the player"
		print(self.name + ':')
		print("health = " + str(self.health))
		print(self.moves)
		print(self.target)
	
	def planMoves(self):
		'deteminds the series of attacks'
		
		#Print++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		print('key  - ','name ',' (length) ',' (damage)')
		for i in range(len(attack)):
			print(i,'  -  ',attack[i],' (',attackLength[attack[i]],') ',' (',attackDamage[attack[i]],') ')
		
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
						if attack[realNumber] == 'doubleKick':
							self.moves[turn] = 'prep'
							self.moves[turn+1] = 'doubleKick'
							skipList.append(turn+1)
							
						elif attack[realNumber] == 'uppercut ':
							for futureTurn in range(attackLength[realNumber]):
								if futureTurn+turn < len(self.moves)-1:
									self.moves[turn+futureTurn] = 'charge'
									skipList.append(turn+futureTurn)	
								if turn+4 < len(self.moves)-1:
									self.moves[turn+4] = 'uppercut '		
							
						else:
							self.moves[turn] = attack[realNumber]
					else:	
						choice = 'null'
						print('try again')
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
		self.health -= amount
		print(self.name + ' has taken ' +str(amount)+' hits')

#======================================================================================================
#funtions==============================================================================================

def setAttacks():
	"defins attacks and give a simple way to turn them off"
	punch     = 'TRUE'
	kick      = 'TRUE'
	blockKick = 'TRUE'
	doubleKick= 'FALSE'
	uppercut  = 'FALSE'
	
	attack.append('none     ')
	attackDamage['none     '] = 0*intensity
	attackLength['none     '] = 1
	if punch     == 'TRUE':
		attack.append('punch    ')
		attackDamage['punch    '] = 1*intensity
		attackLength['punch    '] = 1
	if kick      == 'TRUE':
		attack.append('kick     ')
		attackDamage['kick     '] = 2*intensity
		attackLength['kick     '] = 1
	if blockKick == 'TRUE':
		attack.append('blockKick')
		attackDamage['blockKick'] = 0*intensity
		attackLength['blockKick'] = 1
	if doubleKick== 'TRUE':
		attack.append('doubleKick')
		attackDamage['doubleKick'] = 11*intensity
		attackLength['doubleKick'] = 2
	if uppercut  == 'TRUE':
		attack.append('uppercut ')
		attackDamage['uppercut '] = 9*intensity
		attackLength['uppercut '] = 5
	
	#print(attack)
	#print(attackDamage)
	#print(attackLength)
	
def checkValues():
	"Checks for game breaking inputs"
	if numberOfPlayers > 1 and numberOfMoves > 1 and intensity > 0:
		for damage in attack:
			if attackDamage[damage] <= 0 and damage != 'blockKick' and damage != 'none     ':
				return 'FAlSE'
			else:
				if damage == attack[len(attack)-1]:
					return 'TRUE'
	else:
		return 'FLASE'
		
def battle(what,who,when,person):
	"detiminds the out come of the attacks"
	#if you don't understand the variables :
		#what		=	the attack bieing performed
		#who		=	what player is being attacked
		#when		=	what round/section of a list that is currently happening 
		#person	=	what player is doinf the attack
	if what == 'none     ':
		weird = randint(1, 10) 
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
	elif what == 'prep':
		print(playerList[person].name + ' is preparing for an attack')
	elif what == 'stun':
		print(playerList[person].name +' is stunned')
	elif what == 'charge':
		print(playerList[person].name +' is charging up an attack')
	elif what == 'punch    ':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
	elif what == 'kick     ':
		print(playerList[person].name + ' ' + what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == 'blockKick' and playerList[who].target[when] == person:
			print('but ' + playerList[who].name + ' blocks it')
			playerList[person].moves[when+1] = 'stun'
			print(playerList[person].name + ' is now stunned')
		elif playerList[who].moves[when] == what:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
	elif what == 'blockKick':
		print(playerList[person].name + ' is blocking')
	elif what == 'doubleKick':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		elif playerList[who].moves[when] == 'blockKick' and playerList[who].target[when] == person:
			print('but ' + playerList[who].name + ' blocks it')
			playerList[person].moves[when+1] = 'stun'
			print(playerList[person].name + ' is now stunned')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
	elif what == 'uppercut ':
		print(playerList[person].name + ' '+ what + 'es ' + playerList[who].name)
		if playerList[who].moves[when] == what and playerList[who].target[when]==person:
			print('draw')
		else:
			playerList[who].damage(attackDamage[what])
			if playerList[who].moves[when] == 'prep':
				playerList[who].moves[when+1] = 'stun'
				print(playerList[who].name + ' has lost balence and is now stunned')
		
	else:
		print('value error')
	
def clear(numLines):
	'prints empty lines to flood the screen'
	for helloRobertYouDontNeedToReadThisItsAnEasterEgg in range(numLines):
		print()
#======================================================================================================
#run===================================================================================================


#setup-------------------------------------------------------------------------------------------------
setAttacks()
if checkValues()=='TRUE':
	clear(50)
	for j in range(numberOfPlayers):
		temp = Player(numberOfMoves,totalHealth,str(input('player '+ str(j+1) +' whats your name - ')))	
		playerList.append(temp)
	
	#input-------------------------------------------------------------------------------------------------
	while playerList[0].health>0 and playerList[1].health>0:
		clear(50)
		for j in range(len(playerList)):
			playerList[j].planMoves()
		
			if numberOfPlayers > 2:
				playerList[j].planTarget(playerList)
			else:
				playerList[1].target = [0]*numberOfMoves
				playerList[0].target = [1]*numberOfMoves
			clear(100)
			#playerList[j].info()
			
		
	#run---------------------------------------------------------------------------------------------------
		for number in range(numberOfMoves):
			print('round ' + str(number+1)+' ------------------')
			for player in range(numberOfPlayers):
				battle(playerList[player].moves[number], playerList[player].target[number],number,player)
				#playerList[player].info()
				print()
			
	#outup-------------------------------------------------------------------------------------------------
		for j in range(numberOfPlayers):
			print(playerList[j].name + ' is at '+ str(playerList[j].health))
		input('press enter to continue')
	
	#end+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	for j in range(numberOfPlayers):
		print(playerList[j].name, playerList[j].health,sep=(' - '),end=('.....................'+"\n"))	
else:
	print('Some values in your game are corrupted')


