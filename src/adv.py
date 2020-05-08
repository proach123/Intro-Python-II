from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item('rock',"outside", {'atk': 1})),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[] ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Pat', room['outside'],[])

done = False


def print_help_text():
    print("""
    Valid commands:
        -[n]: move north
        -[s]: move south
        -[e]: move east
        -[w]: move west
        -[q]: quit
        -[i]: inventory
        -[c] or [check]: checks the room for interactiables
        -[get [item name]]: pick up an item
        -[drop [item name]]: drop an item
        -[?] or [help]: help text
    """)


def skip_input():
    print('I dont understand that \n')


while not done:
    print(player.location)
    
    print('\n')
    print(player.location.print_description())
    print('\n')

    
    command = input('type ? for commands. \n')

    if command in ['i']:
        for i in player.player_items:
            print(i)
        continue

    if command in ['c', 'check']:
        print(room['outside'].print_items)
        continue

    if command in ['n', 's', 'e', 'w']:
        player.location = player.move_to(command, player.location)
        continue


    if command in ['q', 'quit', 'exit']:
        done = True

    
    if command in ['?', 'help']:
        print_help_text()
        continue
    else:
        skip_input()
        continue
