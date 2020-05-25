import sys

class Start:
    def __init__(self, display):
        self.display = 'X'

    def step(self, player, direction):
        if direction == "w":
            player.row += 1
        if direction == "s":
            player.row -= 1
        if direction == "a":
            player.col += 1
        if direction == "d":
            player.col -= 1

    def message(self):
        return "\nYou walked into a wall. Oof!\n"

class End:
    def __init__(self, display):
        self.display = 'Y'

    def step(self, player, game):
        pass

    def message(self):
        return "\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n"

class Air:
    def __init__(self, display):
        self.display = ' '

    def step(self, player, game):
        pass

    def message(self):
        return ""

class Wall:
    def __init__(self, display):
        self.display = '*'

    def step(self, player, direction):
        if direction == "w":
            player.row += 1
        if direction == "s":
            player.row -= 1
        if direction == "a":
            player.col += 1
        if direction == "d":
            player.col -= 1

    def message(self):
        return "\nYou walked into a wall. Oof!\n"

class Fire:
    def __init__(self, display):
        self.display = 'F'

    def step(self, player, direction):
        if player.num_water_buckets < 1:
            sys.exit()
        if player.num_water_buckets >= 1:
            player.num_water_buckets -= 1

    def message(self):
        if player.num_water_buckets < 1:
            return "You step into the fires and watch your dreams disappear :("
        if player.num_water_buckets >= 1:
            return "With your strong acorn arms, you throw a bucket of water at the fire. You acorn roll your way through the extinguished flames!"



class Water:
    def __init__(self, display):
        self.display = 'W'

    def step(self, player, direction):
        player.num_water_buckets += 1

    def message(self):
        return "Thank the honourable furious forest, you've found a bucket of water!"

class Teleport:
    
    def __init__(self, display):
        possible_tele = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in possible_tele:
            if i == display:
                self.display = i

    def step(self, player, direction):
        pass

    def message(self):
        return "teleporters not implemented yet"

