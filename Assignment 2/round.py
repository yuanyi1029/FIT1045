from __future__ import annotations
from cards import Card, Rank, Suit


class Round:

    def __init__(self, players: list[Player]) -> None:
        self.players = players

        for player in self.players:  # find who has Two of Clubs
            player.hand.sort()
            if player.hand[0] == Card(Rank.Two, Suit.Clubs):
                leader = player  # assign leader to player who has Two of Clubs
                break

        broken_hearts = False
        # round_score = [0, 0, 0, 0]

        while len(self.players[0].hand) != 0 and len(self.players[0].hand) != 0 and len(
                self.players[0].hand) != 0 and len(self.players[0].hand) != 0:

            turn_order = []
            # finding order of player turn in round
            for i in range(self.players.index(leader), len(self.players)):
                # start from leader append next player till end
                turn_order.append(self.players[i])

            while len(turn_order) != 4:  # append remaining player if it did not append all players in first loop
                for i in range(self.players.index(leader)):  # start from zero (inclusive) to leader (non-inclusive)
                    turn_order.append(self.players[i])

            # print(players)
            # print(turn_order)

            trick = []
            # broken_hearts = False

            for player in turn_order:
                played_card = player.play_card(trick, broken_hearts)
                print(f"{player} plays {played_card}")
                # print(f"{player} plays {trick.played_cards[player]}")
                trick.append(played_card)
                player.hand.pop(player.hand.index(played_card))

                if not broken_hearts:
                    for i in range(len(trick)):
                        if trick[0].suit.value == 4 or (
                                trick[0].suit.value != trick[i].suit.value and trick[i].suit.value == 4):
                            broken_hearts = True
                            print("Hearts have been broken!")

            taker_played_card = trick[0]
            for i in trick:  # finding taker by comparing suit first then rank
                if i.suit.value == taker_played_card.suit.value and i.rank.value > taker_played_card.rank.value:
                    taker_played_card = i

            taker = turn_order[trick.index(taker_played_card)]  # finding taker by taking the index of taker played card
            # print(taker)

            penalty = 0
            for i in trick:
                if i.suit.value == 4:
                    penalty += 1
                elif i == Card(Rank.Queen, Suit.Spades):
                    penalty += 13

            # print(penalty)

            print(f"{taker} takes the trick. Points received: {penalty} points")

            # round_score = [0, 0, 0, 0]
            self.players[self.players.index(taker)].round_score += penalty

            # print(round_score)
            leader = taker

        # total_score = [0, 0, 0, 0]
        # player_index = 0

        # for player in self.players:
        #     print(f"{player}'s score: {player.round_score}")
        #     player.total_score += player.round_score
        #     player.round_score = 0
