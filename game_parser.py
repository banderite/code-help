from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player
#Reads a given file, processes it with parse, and returns the contents as a list of list of cells  
def read_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = []
            for line in file:
                lines.append(line)
            return parse(lines)
    #if file is not found, print this exception
    except FileNotFoundError:
        print("{} does not exist!".format(filename))

def big_parse(gamestate):
    lines = []
    element = ""
    for char in gamestate:
        if char == "\n":
            lines.append(element)
            element = ""
        else:
            element += char
    return parse(lines)



def parse(lines):
    #Checks if there are any illegal letters in the board file, and informs the user what the illegal term is if there is one
    legal_terms = ["A", " ", "X", "Y", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "W", "F"]
    telepads = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    x_count = 0
    y_count = 0
    tele_count = []
    for i in lines:
        i = i.strip("\n")
        for char in i:
            if char == "X":
                x_count += 1
            if char == "Y":
                y_count += 1
            if char in telepads:
                tele_count.append(char)
            if char in legal_terms:
                continue
            #else:
                #raise ValueError("Bad letter in configuration file: {}.".format(char))
    #checks for exactly 1 starting position
    #if x_count != 1:
        #raise ValueError("Expected 1 starting position, got {}.".format(x_count))
    #checks for exactly 1 ending position
    #if y_count != 1:
        #raise ValueError("Expected 1 ending position, got {}.".format(y_count))
    #checks that all teleporters come in pairs
    for telepad in tele_count:
       if tele_count.count(telepad) != 2:
        raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(telepad))
    #makes a list of list of cells
    grid = []
    individual_ls = []
    for i in lines:
        for char in i:
            if char == "A":
                p = Player(0,0)
                individual_ls.append(p)
            if char == "X":
                x = Start("X")
                individual_ls.append(x)
            if char == "Y":
                y = End("Y")
                individual_ls.append(y)
            if char == " ":
                z = Air(" ")
                individual_ls.append(z)
            if char == "*":
                a = Wall("*")
                individual_ls.append(a)
            if char == "F":
                f = Fire("F")
                individual_ls.append(f)
            if char == "W":
                w = Water("X")
                individual_ls.append(w)
            if char in telepads:
                telepad = Teleport("{}".format(char))
                individual_ls.append(telepad)
        grid.append(individual_ls)
        individual_ls = []
    return grid

