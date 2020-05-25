from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from game_parser import read_lines
from game_parser import parse
from player import Player


def grid_to_string(grid, player):
    playing_field = ""
    line = ""
    for level in grid:
        for char in level:
            if char == grid[player.row][player.col]:
                line += player.display
            else:
                line += char.display 

            
        line += "\n"
        playing_field += line
        line = ""
    return playing_field

"""
Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
        """