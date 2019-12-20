import random
import time

##Compares the selected user play and selected robot play from users perspective for victory
def player_plays(selected_user_play, selected_robot_play):
	if selected_user_play == 'Rock' and selected_robot_play == 'Scissors':
		return 'Player wins!'
	elif selected_user_play == 'Scissors' and selected_robot_play == 'Paper':
		return 'Player wins!'
	elif selected_user_play == 'Paper' and selected_robot_play == 'Rock':
		return 'Player wins!'
	else:
		return 'Tie!'

##Compares the selected user play and selected robot play from robots perspective for victory
def robot_plays(selected_robot_play, selected_user_play):
	if selected_robot_play == 'Rock' and selected_user_play == 'Scissors':
		return 'The robot has won!'
	elif selected_robot_play == 'Scissors' and selected_user_play == 'Paper':
		return 'The robot has won!'
	elif selected_robot_play == 'Paper' and selected_user_play == 'Rock':
		return 'The robot has won!'
	else:
		return 'Tie!'

##Assigns random integer 0,1,2 with a string value
def random_robo_play(robotnum):
	if robotnum == 0:
		robot_play = 'Rock'
		return robot_play
	elif robotnum == 1:
		robot_play = 'Scissors'
		return robot_play
	elif robotnum == 2:
		robot_play = 'Paper'
		return robot_play

#Gameplay
while True:
	play_game = input('Are you ready to play Rock, Paper, Scissors? (y/n) ')
	time.sleep(1)
	while play_game == 'y':
		selected_user_play = input('Choose your move! Rock, Paper, or Scissors? ')
		robotnum = random.randint(0,2)
		selected_robot_play = random_robo_play(robotnum)
		time.sleep(1)
		print(f'You selected {selected_user_play}'.format())
		time.sleep(1)
		print(f'The robot selected {selected_robot_play}'.format())
		time.sleep(1)
		game_decision1 = player_plays(selected_user_play, selected_robot_play)
		if game_decision1 == 'Tie!':
			game_decision2 = robot_plays(selected_robot_play, selected_user_play)
			print(game_decision2)
			play_game = input('Play again? (y/n) ')
			if play_game == 'n':
				time.sleep(1)
				print('Thank you for playing!')
				time.sleep(1)
				quit()
		else:
			print('You have won the game! ')
			play_game = input('Play again? (y/n) ')
			if play_game == 'n':
				time.sleep(1)
				print('Thank you for playing!')
				time.sleep(1)
				quit()





