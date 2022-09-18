from __future__ import annotations
from cards import Card, Rank, Suit

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

        for player in self.turn_order(leader):
            played_card = player.play_card(trick, broken_hearts)
            print(f"{player} plays {played_card}")
            trick.append(played_card)

            if broken_hearts is False:
                for i in range(len(trick)):
                    if trick[0].suit.value == 4 or (
                            trick[0].suit.value != trick[i].suit.value and trick[i].suit.value == 4):
                        broken_hearts = True
                        print("Hearts have been broken!") #to pass test case remove this line

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

        print(f"{taker} takes the trick. Points received: {penalty}")

        self.players[self.players.index(taker)].round_score += penalty

        return taker