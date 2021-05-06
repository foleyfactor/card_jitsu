from deck import standard_deck
from game import Game
from player import RandomPlayer, TextPlayer

if __name__ == "__main__":
    human = TextPlayer(standard_deck)
    cpu = RandomPlayer(standard_deck)
    game = Game(human, cpu)
    game.play_full_game()
    print("{} wins!".format(game.winner.name))