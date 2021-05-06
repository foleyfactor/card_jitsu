from player import PlayerID
from state import GameState

class Game(object):
    def __init__(self, player1, player2):
        self.state = GameState()
        self.player1 = player1
        self.player2 = player2
        self.winner = None
    
    def player_select_card(self, player, idx):
        player_card = player.select_card()
        while not self.can_play(player_card, self.state.bans[idx]):
            player.reject_play(player_card)
            player_card = player.select_card()
        player.accept_play(player_card)
        self.state.bans[idx] = None
        return player_card
    
    def can_player_play(self, player, idx):
        for card in player.hand:
            if self.can_play(card, self.state.bans[idx]):
                return True
        return False
    
    def apply_bonuses(self, card1, card2):
        bonus1, bonus2 = self.state.bonuses
        self.state.bonuses = [0, 0]
        return card1.with_number(card1.number + bonus1), card2.with_number(card2.number + bonus2)
    
    def record_win(self, card, idx):
        self.state.inventories[idx.value].add(card)

        if self.state.inventories[idx.value].has_won():
            self.winner = idx

        if card.after_effect is not None:
            card.after_effect(self.state, idx)
    
    def play_round(self):
        if self.winner is not None:
            return
        
        player1 = self.player1
        player2 = self.player2
        
        player1.draw()
        player2.draw()

        if not self.can_player_play(player1, PlayerID.PLAYER1.value):
            return self.set_winner(PlayerID.PLAYER2)
        player1_card = self.player_select_card(player1, PlayerID.PLAYER1.value)

        if not self.can_player_play(player2, PlayerID.PLAYER2.value):
            return self.set_winner(PlayerID.PLAYER1)
        player2_card = self.player_select_card(player2, PlayerID.PLAYER2.value)
    
        if player1_card.turn_effect is not None:
            player1_card, player2_card = player1_card.turn_effect(player1_card, player2_card)

        if player2_card.turn_effect is not None:
            player2_card, player1_card = player2_card.turn_effect(player2_card, player1_card)
        
        player1_card, player2_card = self.apply_bonuses(player1_card, player2_card)

        print()
        print("Player 1 plays:")
        player1_card.display()
        print("Player 2 plays:")
        player2_card.display()
        print()
        
        if player1_card.beats(player2_card):
            self.record_win(player1_card, PlayerID.PLAYER1)
        
        if player2_card.beats(player1_card):
            self.record_win(player2_card, PlayerID.PLAYER2)

    def can_play(self, card, ban):
        return card.element != ban
    
    def play_full_game(self):
        while self.winner is None:
            self.state.display()
            self.play_round()