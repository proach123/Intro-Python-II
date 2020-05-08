# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, player_items):
        self.location = location
        self.name = name
        self.player_items = ['sword', 'shield']



    def move_to(self, direction, current_loc):
        attribute = direction + '_to'
        if hasattr(current_loc, attribute):
            return getattr(current_loc, attribute)
        print("You can't go that way\n")

        return current_loc
    
    # def pick_up(self, current_loc, item):
    #     attribute = 