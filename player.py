from enum import Enum
from random import randint, uniform 

HAND_SIZE = 5

class PlayerID(Enum):
    PLAYER1 = 0
    PLAYER2 = 1

    def opposite(self):
        return PlayerID(1-self.value)

class PlayerBase(object):
    def __init__(self, deck):
        self.hand = []
        self.discard = []
        self.deck = sorted(deck, key=lambda _: uniform(0, 1))
    
    def draw(self):
        while len(self.hand) < HAND_SIZE:
            if not self.deck:
                self.deck = sorted(self.discard, key=lambda _: uniform(0, 1))
                self.discard = []

            self.hand.append(self.deck.pop())

    def reject_play(self, card):
        self.hand.append(card)
    
    def accept_play(self, card):
        self.discard.append(card)

    def select_card(self):
        raise NotImplementedError("cannot select card in a playerbase")

class TextPlayer(PlayerBase):
    def __init__(self, deck):
        super().__init__(deck)
    
    def select_card(self):
        for i in range(len(self.hand)):
            print("{}: ".format(i), end="")
            self.hand[i].display()
        print("Which card do you choose? ", end="")
        while True:
            try:
                i = int(input().strip())
                return self.hand.pop(i)
            except ValueError:
                pass

class RandomPlayer(PlayerBase):
    def __init__(self, deck):
        super().__init__(deck)
    
    def select_card(self):
        return self.hand.pop(randint(0, len(self.hand)-1))