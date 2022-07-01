##################
### Draw board ###
##################

def draw_board(board):
	for i in range(3):
		print(get_symb(board[3*i]), end='')
		print("|", end='')
		print(get_symb(board[3*i + 1]), end='')
		print("|", end='')
		print(get_symb(board[3*i + 2]))
		if (i != 2):
			print("-----")

def get_symb(state):
	if (state == 0):
		return ' '
	elif (state == 1):
		return 'X'
	elif (state == 2):
		return 'O'


#########################
### Board information ###
#########################

def is_full(board):
	for i in board:
		if i == 0:
			return 0
	return 1

def is_legal(board, move):
	return board[move] == 0

def is_winning(board, player):
	for i in range(3):
		if (player == board[3*i] and board[3*i] == board[3*i + 1] and board[3*i + 1] == board[3*i + 2]):
			return 1
	for i in range(3):
		if (player == board[i] and board[i] == board[3 + i] and board[3 + i] == board[6 + i]):
			return 1
	if (player == board[0] and board[0] == board[4] and board[4] == board[8]):
		return 1
	if (player == board[2] and board[2] == board[4] and board[4] == board[6]):
		return 1
	return 0

def init_board():
	return [0 for i in range(9)]

def opponent(player):
	return (player % 2) + 1

def to_arr(board):
	n = 0
	for i in range(9):
		n += 3 ** i * board[i]
	return n

def player_turn(board):
	i = 0
	j = 0
	for k in range(9):
		if (board[k] == 1):
			i += 1
		if (board[k] == 2):
			j += 1

	if (i == j):
		return 1
	return 2
