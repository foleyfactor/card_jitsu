from card import Card, PowerCard
from color import Color
from effect import BanElementEffect
from effect import DiscardOneColorEffect, DiscardElementEffect
from effect import ReversalTurnEffect, SwapElementsTurnEffect
from effect import Plus2Effect, Minus2Effect
from effect import TurnEffect, AfterEffect
from element import Element

standard_deck = [
    Card(Color.BLUE, Element.FIRE, 3),
    Card(Color.GREEN, Element.FIRE, 2),
    Card(Color.GREEN, Element.FIRE, 8),
    Card(Color.ORANGE, Element.FIRE, 3),
    Card(Color.PURPLE, Element.FIRE, 4),
    Card(Color.PURPLE, Element.FIRE, 6),
    Card(Color.RED, Element.FIRE, 2),
    Card(Color.RED, Element.FIRE, 7),
    Card(Color.YELLOW, Element.FIRE, 2),
    Card(Color.YELLOW, Element.FIRE, 5),
    Card(Color.BLUE, Element.SNOW, 3),
    Card(Color.GREEN, Element.SNOW, 2),
    Card(Color.GREEN, Element.SNOW, 5),
    Card(Color.ORANGE, Element.SNOW, 3),
    Card(Color.PURPLE, Element.SNOW, 4),
    Card(Color.PURPLE, Element.SNOW, 8),
    Card(Color.RED, Element.SNOW, 2),
    Card(Color.RED, Element.SNOW, 6),
    Card(Color.YELLOW, Element.SNOW, 2),
    Card(Color.YELLOW, Element.SNOW, 7),
    Card(Color.BLUE, Element.WATER, 3),
    Card(Color.BLUE, Element.WATER, 5),
    Card(Color.GREEN, Element.WATER, 2),
    Card(Color.GREEN, Element.WATER, 8),
    Card(Color.ORANGE, Element.WATER, 3),
    Card(Color.PURPLE, Element.WATER, 4),
    Card(Color.PURPLE, Element.WATER, 6),
    Card(Color.RED, Element.WATER, 2),
    Card(Color.RED, Element.WATER, 7),
    Card(Color.YELLOW, Element.WATER, 2),
    PowerCard(Color.RED, Element.FIRE, 9, TurnEffect.NOOP, BanElementEffect(Element.SNOW)),
    PowerCard(Color.BLUE, Element.FIRE, 9, SwapElementsTurnEffect(Element.WATER, Element.FIRE), AfterEffect.NOOP),
    PowerCard(Color.YELLOW, Element.FIRE, 10, ReversalTurnEffect(), AfterEffect.NOOP),
    PowerCard(Color.ORANGE, Element.FIRE, 10, TurnEffect.NOOP, DiscardElementEffect(Element.SNOW)),
    PowerCard(Color.PURPLE, Element.FIRE, 11, TurnEffect.NOOP, DiscardOneColorEffect(Color.RED)),
    PowerCard(Color.GREEN, Element.FIRE, 11, TurnEffect.NOOP, DiscardOneColorEffect(Color.YELLOW)),
    PowerCard(Color.RED, Element.FIRE, 12, TurnEffect.NOOP, Plus2Effect()),
    PowerCard(Color.BLUE, Element.FIRE, 12, TurnEffect.NOOP, Minus2Effect()),
]