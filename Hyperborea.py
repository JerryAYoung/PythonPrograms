
import random
import time

##Define generalized Monster() class containing seperate monsterattacks and monstername attributes. Inherates Health() & TotalAttacks() classes
class Monster():
	def __init__(self, monstername, healthpoints):
		self.monstername = monstername
		self.healthpoints = healthpoints

##Define generalized Player() class containing seperate playerattacks and playername attributes. Inherates Health() & TotalAttacks() classes
class Player():
	def __init__(self, playername, healthpoints):
		self.playername = playername
		self.healthpoints = healthpoints

##Defined function to randomly select monster to verse!
def random_monster_selector():
	ogre = Monster("Polyphemus", 50)
	medusa = Monster("Euryale", 200)
	golem = Monster("Talos", 150)

	monsterlist = [ogre, medusa, golem]
	randmonster = random.choice(monsterlist)

	if randmonster == ogre:
		nameofmonster = ogre.monstername
		desc_nameofmonster = ogre.monstername
		active_monster_health = ogre.healthpoints
		return randmonster, nameofmonster, desc_nameofmonster + ", the giant son of Poseidon", active_monster_health
	elif randmonster == medusa:
		nameofmonster = medusa.monstername
		desc_nameofmonster = medusa.monstername
		active_monster_health = medusa.healthpoints
		return randmonster, nameofmonster, desc_nameofmonster + ", the 2nd sister of the Gorgons", active_monster_health
	elif randmonster == golem:
		nameofmonster = golem.monstername
		desc_nameofmonster = golem.monstername
		active_monster_health = golem.healthpoints
		return randmonster, nameofmonster, desc_nameofmonster + ", the great bronze guard of Crete", active_monster_health

##Checks if the monster is dead after each attack
def check_mdeath():
	if active_monster_health < 0:
		print(f'You have defeated {desc_nameofmonster}!')
		confirm_death = True
		return confirm_death
	else:
		time.sleep(1)
		print(f"{nameofmonster} now has only {active_monster_health} health left!")
		confirm_death = False
		return confirm_death 

##Checks if the player is dead after each attack
def check_pdeath():
	if player_health < 0:
		print('You have died in combot....')
	else:
		time.sleep(1)
		print(f"You have only {player_health} health left!")
		

##Chooses what attack a monster will use
def m_attack_random():
	m_attacklist = [0,1,2,3,4,5,6]
	m_attackchoice = random.choice(m_attacklist)
	return m_attackchoice

##Intro questions of the game
time.sleep(2)
print("Welcome to 'Hyperborea', A text-based fighting game by REJECT$ Studios.")
time.sleep(3)
playername = input("What will be your name for this adventure? ")
time.sleep(2)
print(f'Hello, {playername}! Let us get started.')
time.sleep(3)

##Define player with Player() class
theplayer = Player(playername, 125) 

randmonster, nameofmonster, desc_nameofmonster, active_monster_health = random_monster_selector()

walking_list = [1,2,3]

for num in walking_list:
	print('Walking...')
	time.sleep(1)

time.sleep(2)
print(f'{playername} has came across {desc_nameofmonster}!')
time.sleep(2)

player_health = theplayer.healthpoints

#Fighting
while active_monster_health > 0:
	time.sleep(1)
	while True:
		try:
			playermove = int(input(f"Choose your attack {playername}! \n1.) Sword Slash | 2.) Punch \n3.) Execute | 4.) Shield Bash \n(1-4): "))
			break
		except:
			print('That is not a move! Choose 1-4!')
		
	if active_monster_health > 0:
		##Sword Slash
		if playermove == 1:
			active_monster_health = active_monster_health - 20
			time.sleep(2)
			print(f"{playername} has slashed {nameofmonster} dealing 20 damage!")
			confirm_death = check_mdeath()
			if confirm_death == True:
				break
			else:
				m_attackchoice = m_attack_random()
		##Punch
		elif playermove == 2:
			active_monster_health = active_monster_health - 5
			time.sleep(2)
			print(f"{playername} has punched {nameofmonster} dealing 5 damage!")
			confirm_death = check_mdeath()
			if confirm_death == True:
				break
			else:
				m_attackchoice = m_attack_random()
		##Execute
		elif playermove == 3:
			active_monster_health = active_monster_health - 35
			time.sleep(2)
			print(f"{playername} has executed {nameofmonster} dealing 35 damage!")
			confirm_death = check_mdeath()
			if confirm_death == True:
				break
			else:
				m_attackchoice = m_attack_random()
		##Shield Bash
		elif playermove == 4:
			active_monster_health = active_monster_health - 15
			time.sleep(2)
			print(f"{playername} has bashed {nameofmonster} with their shielf dealing 15 damage!")
			confirm_death = check_mdeath()
			if confirm_death == True:
				break
			else:
				m_attackchoice = m_attack_random()
		else:
			print('You have missed your attack!')
			m_attackchoice = m_attack_random()

	if player_health > 0:
		if m_attackchoice == 0:
			player_health = player_health - 45
			time.sleep(2)
			print(f"{nameofmonster} has thrown a boulder at you, you are dealt 45 damage!")
			check_pdeath()
		##Punch
		elif m_attackchoice == 1:
			player_health = player_health - 5
			time.sleep(2)
			print(f"{nameofmonster} has swiped you, you are dealt 5 damage!")
			check_pdeath()
		##Execute
		elif m_attackchoice == 2:
			player_health = player_health - 15
			time.sleep(2)
			print(f"{nameofmonster} has bit you, you are dealt 15 damage!")
			check_pdeath()
		##Shield Bash
		elif m_attackchoice == 3:
			player_health = player_health - 35
			time.sleep(2)
			print(f"{nameofmonster} has summoned their allies to slash you, you are dealt 35 damage!")
			check_pdeath()
		elif m_attackchoice == 4:
			player_health = player_health - 25
			time.sleep(2)
			print(f"{nameofmonster} has headbutted you, you are dealt 25 damage!")
			check_pdeath()
		elif m_attackchoice == 5:
			player_health = player_health - 10
			time.sleep(2)
			print(f"{nameofmonster} has thrown you to the ground, you are dealt 10 damage!")
			check_pdeath()
		else:
			print(f"{nameofmonster} has missed their attack!")
			time.sleep(2)





