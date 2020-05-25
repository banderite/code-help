from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game_parser import read_lines, big_parse
from grid import grid_to_string
from player import Player
import os
import sys

boardin = "board_simple.txt"


def start_pos(board):
	parsed_board = read_lines(board)
	global i
	i = 0
	while i < len(parsed_board):
		global j
		j = 0
		while j < len(parsed_board[i]):
			if type(parsed_board[i][j]) == Start:
				global protag
				protag = Player(i, j)
			j += 1
		i += 1
	return grid_to_string(parsed_board, protag) + "\nYou have {} water buckets.".format(protag.num_water_buckets)

def game_move(boardstate, direction):
	protag.move(direction)
	parsed_board = big_parse(boardstate)
	#print(parsed_board)
	result = grid_to_string(parsed_board, protag)
	return result

#places player at starting position
starting_position = start_pos(boardin)
print(starting_position)

#first move
move = input("Input a direction: ")
board_state = game_move(starting_position, move)
print(board_state)



while True:
	move = input("Input a direction: ")
	a = game_move(board_state, move)
	print(a)
	board_state = a