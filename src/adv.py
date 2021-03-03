from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player_name = input("What is your character's name? ")
player = Player(player_name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f"Welcome {player.name}! Can you find find the treasure room in this dungeon?")

possible_commands = """
"q" = quit
"n" = move north
"e" = move east 
"s" = move south
"w" = move west
"""

def move_north():
    player.current_room = player.current_room.n_to
    
def move_east():
    player.current_room = player.current_room.e_to
    
def move_south():
    player.current_room = player.current_room.s_to
    
def move_west():
    player.current_room = player.current_room.w_to
    
def print_help():
    print(possible_commands)

def take_commands(action):
    actions = {
        "n" : move_north,
        "e" : move_east,
        "s" : move_south, 
        "w" : move_west,
        "h" : print_help
    }
    if action not in actions:
        print("That is not a valid command")
        return
    actions[action]()

while True: 
    print(f"You are in the {player.current_room.name}")
    command = input("Enter a command (h = help): ")
    if command.lower() == "q":
        break
    else:
        take_commands(command.lower())
    

    