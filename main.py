###############
### Imports ###
###############

from move import *
from tic_tac_toe import *
from q_learning import *




def learn(learn_time=100000):
	print("Learning ...")

	# Load Q table
	Q = load_Q_table()

	# Let AI play against itself
	for j in range(learn_time):
		# Feedback
		if (j % min(10000, learn_time/10) == 0):
			print("Played", j, "games")
			store_Q_table(Q)


		# Initialise board and player
		board = init_board()
		board_history = [board[:]]
		move_history = []
		player = 1

		# Play game
		while((not is_full(board)) and (not is_winning(board, opponent(player)))):

			# AI choose move
			m = move()
			while (not is_legal(board, m)):
				Q_learning_illegal(Q, board, m, rewards)
				m = move()

			# Update board
			board[m] = player
			player = opponent(player)

			board_history.append(board[:])
			move_history.append(m)

		# Update Q table after game
		Q = Q_learning_revision(Q, board_history[:-1], move_history, rewards)

	# Save data to file
	store_Q_table(Q)


def play():

	print("Ready to play")
	# Initialise board and player
	board = init_board()
	player = 1


	# Load Q table
	Q = load_Q_table()

	draw_board(board)
	while((not is_full(board)) and (not is_winning(board, opponent(player)))):

		# Show Q table
		for i in range(3):
			f1 = "{:.2f}".format(Q[to_arr(board)][3*i])
			f2 = "{:.2f}".format(Q[to_arr(board)][3*i + 1])
			f3 = "{:.2f}".format(Q[to_arr(board)][3*i + 2])

			print(f1, f2, f3, sep='\t')

		# Get players move
		if (player == 1):
			print("Player move")
			m = player_move(board)
		elif (player == 2) :
			print("A.I. move")
			m = best_move(Q, board, player)


		# Update board
		board[m] = player
		player = opponent(player)
		draw_board(board)



####################
### Main Program ###
####################

if __name__ == "__main__":
	# Trying to converge the Q-table
	learn(1000000)
	play()
