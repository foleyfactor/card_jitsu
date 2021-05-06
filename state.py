from inventory import Inventory

class GameState(object):
    def __init__(self):
        self.inventories = [Inventory(), Inventory()]
        self.bonuses = [0, 0]
        self.bans = [None, None]
    
    def display(self):
        print("Player 1")
        print("Bonus: {}, Ban: {}".format(self.bonuses[0], self.bans[0]))
        self.inventories[0].display()
        print()
        print("Player 2")
        print("Bonus: {}, Ban: {}".format(self.bonuses[1], self.bans[1]))
        self.inventories[1].display()
        print()