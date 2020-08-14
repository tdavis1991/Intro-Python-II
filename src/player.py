# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, items=[], room):
        self.name = name
        self.items = items
        self.room = room

    def __str__(self):
        return f'{self.name} is currently in the {self.room}'
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, index):
        self.items.pop(index)
    
    def view_items(self):
        print(self.items)
