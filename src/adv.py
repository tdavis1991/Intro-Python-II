# from room import Room
# from player import Player
class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def __str__(self):
        return f'{self.name} is currently in the {self.room}'
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, index):
        print(f'Chose item to remove: {self.items}')
        self.items.pop(index)
    
    def view_items(self):
        print(f'Current items: {self.items}')

class Room:
    def __init__(self, name, description, treasure=[]):
        self.name = name
        self.description = description
        self.treasure = treasure

# Declare all the rooms

# Declare all the rooms
treasure_room_items = ['1. jewels', '2. gold']
overlook_items = ['1. shield', '2. armor']
foyer_items = ['1. sword', '2. elixir']

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", foyer_items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", overlook_items),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", treasure_room_items),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].w_to = None
room['outside'].e_to = None
room['outside'].s_to = None

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = None

room['overlook'].s_to = room['foyer']
room['overlook'].n_to = None
room['overlook'].e_to = None
room['overlook'].sw_to = None

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].s_to = None
room['narrow'].e_to = None

room['treasure'].s_to = room['narrow']
room['treasure'].e_to = None
room['treasure'].n_to = None
room['treasure'].w_to = None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
tevin = Player('Tevin', room['outside'])

# Write a loop that:
while True:

#
# * Prints the current room name
    if tevin.room == None:
        print('This is a dead end')
    else:
        print(f'{tevin.room.name}')
# * Prints the current description (the textwrap module might be useful here).
        print(f'{tevin.room.description}')
# * Waits for user input and decides what to do.
    value = input('Please choose one of these directions (n, s, w, e, items, remove or q to quit):\n')
    if value in {'n', 's', 'w', 'e', 'items', 'q'}:
        if value == 'n':
            if tevin.room.n_to is not None:
                tevin.room = tevin.room.n_to
                print(f'You have entered {tevin.room.name}')
                if tevin.room.treasure:              
                    print(f'You have found: {tevin.room.treasure}')
                    chose_item = input('Chose an item to pick up or c to continue\n')
                    tevin.add_item(tevin.room.treasure[int(chose_item)-1])
            else:
                print('This is a dead end')

        elif value == 's':
            if tevin.room.s_to is not None:
                tevin.room = tevin.room.s_to
                print(f'You have entered {tevin.room.name}')
                if tevin.room.treasure:
                    print(f'You have found: {tevin.room.treasure}')
                    chose_item = input('Chose an item to pick up or c to continue\n')
                    tevin.add_item(tevin.room.treasure[int(chose_item)-1])   
            else:
                print('This is a dead end')                  
            
        elif value == 'w':
            if tevin.room.w_to is not None:
                tevin.room = tevin.room.w_to
                print(f'You have entered {tevin.room.name}')
                if tevin.room.treasure:
                    print(f'You have found: {tevin.room.treasure}')
                    chose_item = input('Chose an item to pick up or c to continue\n')
                    tevin.add_item(tevin.room.treasure[int(chose_item)-1])
            else:
                print('This is a dead end')

        elif value == 'e':
            if tevin.room.s_to is not None:
                tevin.room = tevin.room.e_to
                print(f'You have entered {tevin.room.name}')
                if tevin.room.treasure:
                    print(f'You have found: {tevin.room.treasure}')
                    chose_item = input('Chose an item to pick up or c to continue\n')
                    tevin.add_item(tevin.room.treasure[int(chose_item)-1])
            else:
                print('This is a dead end')
        
        elif value == 'items':
            tevin.view_items()
        
        elif value == 'remove':
            remove_item = input('Chose item to remove\n')
            tevin.remove_item(int(remove_item))

        elif value == 'q':
            print(f'{tevin.name}, thank you for playing!')
            break
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
