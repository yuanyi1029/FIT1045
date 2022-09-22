from __future__ import annotations
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer

global broken_hearts


class Round:

    def __init__(self, players: list[Player]) -> None:
        self.players = players

        self.main()

    def main(self):
        global broken_hearts
        broken_hearts = False
        leader = self.first_leader()
        while len(self.players[0].hand) != 0:
            leader = self.taker(leader, self.execute_round(leader))

    def first_leader(self):
        for player in self.players:  # find who has Two of Clubs
            player.hand.sort()
            if player.hand[0] == Card(Rank.Two, Suit.Clubs):
                return player  # return player who has Two of Clubs

    def turn_order(self, leader):
        turn_order = []
        # finding order of player turn in round

        for i in range(self.players.index(leader), len(self.players)):
            # start from leader append next player till end
            turn_order.append(self.players[i])

        while len(turn_order) != len(self.players):
            # append remaining player if it did not append all players in first loop
            for i in range(self.players.index(leader)):  # start from zero (inclusive) to leader (non-inclusive)
                turn_order.append(self.players[i])

        return turn_order

    def execute_round(self, leader):
        global broken_hearts
        trick = []

        count = 0  # new
        for player in self.turn_order(leader):
            played_card = player.play_card(trick, broken_hearts)
            if count == 0:  # new
                print(f"{player} leads with {played_card}")  # new
            else:  # new
                print(f"{player} plays {played_card}")
            trick.append(played_card)
            count += 1  # new

            if broken_hearts is False:
                for i in range(len(trick)):
                    if trick[0].suit.value == 4 or (
                            trick[0].suit.value != trick[i].suit.value and trick[i].suit.value == 4):
                        broken_hearts = True
                        print("Hearts have been broken!")

        return trick

    def taker(self, leader, trick):

        taker_played_card = trick[0]

        for card in trick:  # finding taker by comparing suit first then rank
            if card.suit.value == taker_played_card.suit.value and card.rank.value > taker_played_card.rank.value:
                taker_played_card = card

        taker = self.turn_order(leader)[trick.index(taker_played_card)]
        # finding taker by taking the index of taker played card

        penalty = 0
        for card in trick:
            if card.suit.value == 4:
                penalty += 1
            elif card == Card(Rank.Queen, Suit.Spades):
                penalty += 13

        print(f"{taker} takes the trick. Points received: {penalty} points")

        self.players[self.players.index(taker)].round_score += penalty

        return taker


# # using our basic AI player that always plays the least ranking valid card
# players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4")]
# players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs),
#                    Card(Rank.Ace, Suit.Hearts)]
# players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades),
#                    Card(Rank.Six, Suit.Diamonds)]
# players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds),
#                    Card(Rank.Queen, Suit.Spades)]
# players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds),
#                    Card(Rank.King, Suit.Hearts)]

# Round(players)
