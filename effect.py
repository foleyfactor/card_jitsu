# TurnEffects don't mutate card values, they return new cards
class TurnEffect(object):
    def __init__(self, fn, name):
        self.fn = fn
        self.name = name
    
    def __call__(self, friendly_card, opponent_card):
        return self.fn(friendly_card, opponent_card)
    
    def __str__(self):
        if self.name is not None:
            return "Effect: {} this turn".format(self.name)
        return ""

TurnEffect.NOOP = TurnEffect(lambda friendly, opponent: (friendly, opponent), None)

class SwapElementsTurnEffect(TurnEffect):
    def __init__(self, from_element, to_element):
        def effect(friendly_card, opponent_card):
            if friendly_card.element == from_element:
                friendly_card = friendly_card.with_element(to_element)
            if opponent_card.element == from_element:
                opponent_card = opponent_card.with_element(to_element)
            return friendly_card, opponent_card
        
        super().__init__(effect, "{} becomes {}".format(from_element.name, to_element.name))

class ReversalTurnEffect(TurnEffect):
    def __init__(self):
        def effect(friendly_card, opponent_card):
            return (friendly_card.with_number(-friendly_card.number), opponent_card.with_number(-opponent_card.number))
        
        super().__init__(effect, "lower cards win")

# AfterEffects are mutators: they do not produce any values but instead mutate the game state which is passed to them
class AfterEffect(object):
    def __init__(self, fn, name):
        self.fn = fn
        self.name = name
    
    def __call__(self, state, idx):
        return self.fn(state, idx)
    
    def __str__(self):
        if self.name is not None:
            return "If this card wins: {}".format(self.name)
        return ""


AfterEffect.NOOP = AfterEffect(lambda state, _: None, None)

class BonusEffect(AfterEffect):
    def __init__(self, delta, to_self, name):
        def effect(state, idx):
            if not to_self:
                idx = idx.opposite()
            state.bonuses[idx.value] = delta

        super().__init__(effect, name)

class Plus2Effect(BonusEffect):
    def __init__(self):
        super().__init__(2, to_self=True, name="+2 to your next turn")

class Minus2Effect(BonusEffect):
    def __init__(self):
        super().__init__(-2, to_self=False, name="-2 to your opponent's next turn")

class DiscardElementEffect(AfterEffect):
    def __init__(self, element):
        def effect(state, idx):
            idx = idx.opposite()
            state.inventories[idx.value].remove_one_element(element)

        super().__init__(effect, "discard one opponent {} card".format(element.name))

class DiscardOneColorEffect(AfterEffect):
    def __init__(self, color):
        def effect(state, idx):
            idx = idx.opposite()
            state.inventories[idx.value].remove_one_color(color)
        
        super().__init__(effect, "discard one opponent {} card".format(color.name))

class DiscardAllColorEffect(AfterEffect):
    def __init__(self, color):
        def effect(state, idx):
            idx = idx.opposite()
            state.inventories[idx.value].remove_all_color(color)
        
        super().__init__(effect, "discard all opponent {} cards".format(color.name))

class BanElementEffect(AfterEffect):
    def __init__(self, element):
        def effect(state, idx):
            idx = idx.opposite()
            state.bans[idx.value] = element
        
        super().__init__(effect, "opponent cannot play {} cards next turn".format(element.name))