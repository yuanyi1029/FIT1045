from __future__ import annotations
import random
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from test import Round


class Hearts:

    def __init__(self) -> None:
        self.players = []
        self.target = int(input("Please enter a target score to end the game: "))
        self.number_of_players = int(input("Please enter the number of players (3-5): "))

        valid_number_of_players = False
        while not valid_number_of_players:
            if 3 <= self.number_of_players <= 5:
                valid_number_of_players = True
            else:
                self.number_of_players = int(input("Please enter the number of players (3-5): "))

        self.game(self.target, self.number_of_players)



    def game(self, target, number_of_players):

        round = 1 

        # create player objects depending on number of players
        for i in range(1, number_of_players+1):
            self.players.append(BasicAIPlayer("Player " + str(i)))
        
        # deal cards to players amd check hands
        self.dealcards(number_of_players, self.players)
        self.playerhandcheck(number_of_players, self.players)

        # game starts 
        print(f"========= Starting round {round} =========")
        for i in self.players: 
            print(f"{i.name} was dealt {i.hand}" )

        Round(self.players)
        print(f"========= End of round {round} =========")
        

        # print(self.players[0].hand)
        # print(self.players[1].hand)
        # print(self.players[2].hand)
        # print(self.players[3].hand)

        # print("test")
        # print(self.players[0].hand)
        # Round(self.players)

        # r1 = Round(self.players)
        # print(r1.one_round())
        # pass cards to players 
        # print(players)



    def dealcards(self, number_of_players: int, players: list[Player]) -> None:
        full_deck = []
        shuffled_deck = []

        # create deck of 52 cards
        for eachsuit in Suit:
            for eachrank in Rank:
                full_deck.append(Card(eachrank, eachsuit))

        #shuffle deck
        for i in range(len(full_deck)):
            selected = random.choice(full_deck)
            shuffled_deck.append(selected)
            full_deck.remove(selected)

        # remove cards for 3 players or 5 players 
        if number_of_players == 3:
            shuffled_deck.remove(Card(Rank.Two, Suit.Diamonds))

        elif number_of_players == 5:
            shuffled_deck.remove(Card(Rank.Two, Suit.Diamonds))
            shuffled_deck.remove(Card(Rank.Two, Suit.Spades))

        # hand out cards
        while len(shuffled_deck) != 0 :
            for player in players:
                player.hand.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])

    def playerhandcheck(self, number_of_players: int, players: list[Player]):
        
        all_valid = True 

        for eachplayer in players:
            player_valid = False 	
            for eachcard in eachplayer.hand:
                if eachcard.suit == Suit.Clubs or eachcard.suit == Suit.Diamonds or (eachcard.suit == Suit.Spades and eachcard != Card(Rank.Queen, Suit.Spades)):
                    player_valid = True 

            if player_valid == False:
                all_valid = False

        if all_valid == False:
            # reset all players hand
            for i in players:
                i.hand = []
            # deal cards again
            self.dealcards(number_of_players, self.players)			

    
if __name__ == "__main__":

    Hearts()


