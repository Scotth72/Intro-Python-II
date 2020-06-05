# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = items

    def inventory(self):
        print(len(self.items))
        if len(self.items) > 0:
            player_items = [item.name for item in self.items]
            return player_items
            print(f"Inventory: {player_items}")
        else:
            print("Nothing in inventory")

    def pick_up_item(self, item):
        self.items.append(item)
        print(self.items)

    def drop_item(self, item):
        self.items = list(
            filter(lambda x: x.name is not item.name, self.items))
