###############
### Imports ###
###############

import pickle
from tic_tac_toe import *




###########################
### Load and Store data ###
###########################

def load_Q_table():
	try :
		with open('Q_table', 'rb') as f:
			Q = pickle.load(f)
	except :
		Q = [[0 for i in range(9)] for i in range(3 ** 9)]

	return Q


def store_Q_table(Q):
	f = open("Q_table", "wb")
	pickle.dump(Q, f)
	f.close



##################
### Q-learning ###
##################

rewards = {
	"win"		: 100,
	"lose"		: -100,
	"illegal"	: -1000000,
	"nothing"	: 0
}

def Q_learning_revision(Q, board_history, move_history, rewards, alpha=0.4, gamma=1):

	board_history.reverse()
	move_history.reverse()
	for move, board in enumerate(board_history):
		# Calculate rewards
		rew = rewards["nothing"]

		# Check if winning move
		next_board = board[:]
		next_board[move_history[move]] = player_turn(board)
		if (is_winning(next_board, player_turn(board))):
			rew = rewards["win"]

		# Check if opponent can win
		
		else :
			for i in range(9):
				opp_board = next_board[:]
				if is_legal(opp_board, i):
					opp_board[i] = opponent(player_turn((board)))
					if (is_winning(opp_board, opponent(player_turn(board)))):
						rew = rewards["lose"]
						break
		


		est = 0
		if (rew == rewards["nothing"]):
			# Calculate estimations
			est = float("-inf")
			for i in range(9):
				if is_legal(next_board, i):
					est = max(Q[to_arr(next_board)][i], est)

			if est == float("-inf"):
				est = 0

		
		Q[to_arr(board)][move_history[move]] = (1 - alpha) * Q[to_arr(board)][move_history[move]] + alpha * (rew + gamma * est)


	return Q

def Q_learning_illegal(Q, board, move, rewards):
	Q[to_arr(board)][move] = rewards["illegal"]
	return Q
