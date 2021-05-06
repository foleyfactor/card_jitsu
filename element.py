from enum import Enum

class Element(Enum):
    FIRE = 0
    WATER = 1
    SNOW = 2

    def beats(self, other):
        return self.value == (other.value + 1) % 3
    
    def ties(self, other):
        return self.value == other.value