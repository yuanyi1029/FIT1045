from __future__ import annotations
from basic_ai import BasicAIPlayer
from round import Round
from cards import Card, Rank, Suit
import random


class Hearts:

    def __init__(self) -> None:

        target_score = int(input("Please enter a target score to end the game: "))

        player_number = int(input("Please enter the number of players (3-5): "))
        valid_player_number = False

        while not valid_player_number:
            if 3 <= player_number <= 5:
                valid_player_number = True
            else:
                player_number = int(input("Please enter the number of players (3-5): "))

        game_end = False

        round = 1

        players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"),
                   BasicAIPlayer("Player 4"), BasicAIPlayer("Player 5")]

        for i in range(5 - player_number):
            players.pop()

        while not game_end:

            deck = [Card(Rank.Two, Suit.Clubs), Card(Rank.Three, Suit.Clubs), Card(Rank.Four, Suit.Clubs),
                    Card(Rank.Five, Suit.Clubs), Card(Rank.Six, Suit.Clubs), Card(Rank.Seven, Suit.Clubs),
                    Card(Rank.Eight, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ten, Suit.Clubs),
                    Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Clubs), Card(Rank.King, Suit.Clubs),
                    Card(Rank.Ace, Suit.Clubs), Card(Rank.Two, Suit.Diamonds), Card(Rank.Three, Suit.Diamonds),
                    Card(Rank.Four, Suit.Diamonds), Card(Rank.Five, Suit.Diamonds), Card(Rank.Six, Suit.Diamonds),
                    Card(Rank.Seven, Suit.Diamonds), Card(Rank.Eight, Suit.Diamonds), Card(Rank.Nine, Suit.Diamonds),
                    Card(Rank.Ten, Suit.Diamonds), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Diamonds),
                    Card(Rank.King, Suit.Diamonds), Card(Rank.Ace, Suit.Diamonds), Card(Rank.Two, Suit.Spades),
                    Card(Rank.Three, Suit.Spades), Card(Rank.Four, Suit.Spades), Card(Rank.Five, Suit.Spades),
                    Card(Rank.Six, Suit.Spades), Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades),
                    Card(Rank.Nine, Suit.Spades), Card(Rank.Ten, Suit.Spades), Card(Rank.Jack, Suit.Spades),
                    Card(Rank.Queen, Suit.Spades), Card(Rank.King, Suit.Spades), Card(Rank.Ace, Suit.Spades),
                    Card(Rank.Two, Suit.Hearts), Card(Rank.Three, Suit.Hearts), Card(Rank.Four, Suit.Hearts),
                    Card(Rank.Five, Suit.Hearts), Card(Rank.Six, Suit.Hearts), Card(Rank.Seven, Suit.Hearts),
                    Card(Rank.Eight, Suit.Hearts), Card(Rank.Nine, Suit.Hearts), Card(Rank.Ten, Suit.Hearts),
                    Card(Rank.Jack, Suit.Hearts), Card(Rank.Queen, Suit.Hearts), Card(Rank.King, Suit.Hearts),
                    Card(Rank.Ace, Suit.Hearts)]

            if player_number == 3:
                deck.pop(deck.index(Card(Rank.Two, Suit.Diamonds)))

            elif player_number == 5:
                deck.pop(deck.index(Card(Rank.Two, Suit.Diamonds)))
                deck.pop(deck.index(Card(Rank.Two, Suit.Spades)))

            random.shuffle(deck)
            # print(deck);
            # print(players)

            while len(deck) != 0:
                for player in players:
                    player.hand.append(deck[0])
                    deck.pop(0)

            print(f"========= Starting round {round} =========")

            for player in players:
                print(f"{player} was dealt {player.hand}")

            if round % len(players) != 0:
                pass_card_list = []
                for player in players:
                    pass_card_list.append(player.pass_cards())

                # print(pass_card_list)

                index_list = []
                for i in range(round % len(players), len(players)):  # from index == round to end
                    # print((players.index(player) + round) % len(players))  # original algorithm

                    players[i].hand += pass_card_list[i - (round % len(players))]  # concatenate list
                    # algorithm: index minus round(modulo with len(player))
                    index_list.append(i - (round % len(players)))

                    # print(i - (round % len(players)))

                # print(index_list)

                pass_card_reverse_index = 1
                # print()
                for i in range((round % len(players) - 1), -1, -1):
                    # remaining players before index that haven't swapped hands (in reverse)
                    players[i].hand += pass_card_list[len(pass_card_list) - pass_card_reverse_index]  # concatenate list
                    # append remaining from last element

                    index_list.insert(0, (len(pass_card_list) - pass_card_reverse_index))
                    # print(len(pass_card_list) - pass_card_reverse_index)

                    pass_card_reverse_index += 1

                print(index_list)
                for i in range(len(players)):
                    print(f"{players[i]} passed {pass_card_list[i]} to {players[index_list.index(i)]}")
                    # passing player of index of target in index_list

            # for player in players:
            #     print(player.hand)

            Round(players)

            print(f"========= End of round {round} =========")

            shot_the_moon = False

            for player in players:
                if player.round_score == 26:
                    shot_the_moon = True
                    print(f"{player} has shot the mooon! Everyone else receives 26 points")

            if shot_the_moon:
                for player in players:
                    if player.round_score == 0:
                        player.round_score = 26
                    elif player.round_score == 26:
                        player.round_score = 0

            for player in players:
                player.total_score += player.round_score
                player.round_score = 0
                print(f"{player}'s total score: {player.total_score}")

            total_score_list = []
            for player in players:
                total_score_list.append(player.total_score)
                if player.total_score >= target_score:
                    game_end = True

            # if len(set(total_score_list)) != len(players):  # using set to see no duplication of score
            #     game_end = False

            winner_count = total_score_list.count(min(total_score_list))
            # print(winner_count)
            if winner_count != 1:
                game_end = False

            round += 1

        winning_player = players[0]
        for player in players:
            if player.total_score < winning_player.total_score:
                winning_player = player

        print(f"{winning_player} is the winner!")


if __name__ == "__main__":
    Hearts()