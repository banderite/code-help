#START HERE
#In a nutshell, this is a game played through the terminal.
#The way the game is meant to work, is that it inputs a text file which is the "board", or play area of the game
#After inputting the text file, the read_lines() function is called on the board, which runs it through a parser,
#which converts the text file strings into game objects (see game_parser.py for detail), in a grid.
#The list of game objects is in the cell file, so "X" = starting position, "*" are the walls, " " is air, etc.
#After converting all the string objects into game objects, the game then does any logic associated with the move inputted by the player
#(e.g. did they hit a wall, did they step on fire, etc.)
#After that, the grid is turned back into a string representation using the grid_to_string() function, see grid.py for more detail
#The grid is then returned to the player on screen, where they are again asked for their next move


#THE PROBLEM
#If you try running the code as it is, you'll notice that the player ("A") stays wherever it was and replaces the object there with a player object
#(see photo in github for an example)
#From what I understand, this is because the code is taking in the string representation of what the player sees, including the player object "A",
#and then parses that through the parser, causing the player object to be "embedded" in the board, while also moving the player
#However, I don't know how I should fix this


#Imports the necessary modules
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

#This is where you put whatever board you are using in
boardin = "board_simple.txt"

#This function sets up the board and places the player (A) on the starting location (X)
def start_pos(board):
	#uses read_lines() to parse the board and turn it from strings into game objects
	parsed_board = read_lines(board)
	#the following finds the coordinates of the start (X), and sets the player's coordinates to it
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
	#finally, the function returns the string representation of the board with the character on it
	return grid_to_string(parsed_board, protag) + "\nYou have {} water buckets.".format(protag.num_water_buckets)

#This function moves the player
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


#loop for all remaining moves
while True:
	move = input("Input a direction: ")
	a = game_move(board_state, move)
	print(a)
	board_state = a