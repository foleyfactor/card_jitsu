from effect import TurnEffect, AfterEffect

class CardBase(object):
    def __init__(self, color, element, number, turn_effect, after_effect):
        self.color = color
        self.element = element
        self.number = number
        self.turn_effect = turn_effect
        self.after_effect = after_effect
    
    def with_element(self, element):
        return CardBase(self.color, element, self.number, self.turn_effect, self.after_effect)
    
    def with_number(self, number):
        return CardBase(self.color, self.element, number, self.turn_effect, self.after_effect)
    
    def beats(self, other):
        return self.element.beats(other.element) or (self.element.ties(other.element) and self.number > other.number)
    
    def display(self):
        print("{} {} ({}). {}{}".format(
            self.color.name, self.element.name, self.number, str(self.turn_effect), str(self.after_effect)
        ))

class Card(CardBase):
    def __init__(self, color, element, number):
        assert(2 <= number <= 8)
        super().__init__(color, element, number, TurnEffect.NOOP, AfterEffect.NOOP)

class PowerCard(CardBase):
    def __init__(self, color, element, number, turn_effect, after_effect):
        assert(9 <= number <= 12)
        super().__init__(color, element, number, turn_effect, after_effect)

class TurnPowerCard(PowerCard):
    def __init__(self, color, element, number, turn_effect):
        super().__init__(color, element, number, turn_effect, AfterEffect.NOOP)

class AfterPowerCard(PowerCard):
    def __init__(self, color, element, number, after_effect):
        super().__init__(color, element, number, TurnEffect.NOOP, after_effect)