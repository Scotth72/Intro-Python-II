from room import Room
from player import Player
from items import Item

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
# add room
room['outside'].items.append("dagger")
# add items
item = {
    "dagger": Item("dagger", "small bladed knife")
}
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("ReadyPlayer1", room["outside"], [])
# Write a loop that:
#
choice = None
moved = True
print(f"Your Adventure Awaits!")
while choice not in ["q"]:
    print(f"Current room has {player.room.items}")
    print(f"{player.inventory()} is in your inventory")
    print(f"You are in {player.room.name}")
    choice = input("choose n,s,e,w to MOVE, grab to GRAB, OR q to quit")
    choice_arr = choice.split(" ")
    choice_len = len(choice_arr)
    print(choice_len)
    if moved:
        if choice in ["n"] and hasattr(player.room, 'n_to'):
            player.room = player.room.n_to
        elif choice in ["s"] and hasattr(player.room, 's_to'):
            player.room = player.room.s_to
        elif choice in ["e"] and hasattr(player.room, 'e_to'):
            player.room = player.room._to
        elif choice in ["w"] and hasattr(player.room, 'w_to'):
            player.room = player.room.w_to
        elif choice in ["q"]:
            print(f"Comeback and play again")
            moved = False
        else:
            print("Try again, unable to move that way")

    if choice_len == 2:
        action = choice_arr[0]
        item = choice_arr[1]
        if action in ["grab"]:
            try:
                player.pick_up_item(item[item])
            except:
                print("No item to grab")

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
