###############
### Imports ###
###############

import random as rd
from tic_tac_toe import *


###################
### A.I. choice ###
###################

def player_move(board):
	m = int(input("Your turn :"))
	while (not is_legal(board, m)):
		m = int(input("Your turn :"))
	return m


def move():
	return rd.randrange(9)

def best_move(Q, board, player):
	tried_moves = []
	est = float("-inf")
	m = -1
	for i in range(9):
		if Q[to_arr(board)][i] > est:
			m = i
			est = Q[to_arr(board)][i]
	while (not is_legal(board, m)):
		tried_moves.append(m)
		est = float("-inf")
		m = -1
		for i in range(9):
			if (not i in tried_moves) and Q[to_arr(board)][m] > est:
				m = i
				est = Q[to_arr(board)][m]
	return m
