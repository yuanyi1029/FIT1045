from __future__ import annotations
from basic_ai import BasicAIPlayer
from round import Round
from cards import Card, Rank, Suit
import random

global round


def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input
    can also be restricted to a set of integers.

    Arguments:
      - prompt: String representing the message to display for input
      - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)  #
        # if type(player_input) != int: continue
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input


def card_interface(card_list):
    suit_art = {
        1: "│  ♣  │",
        2: "│  ♦  │",
        3: "│  ♠  │",
        4: "│  ♥  │"
    }

    rank_art = {
        2: ["┌─────┐", "│2    │", "       ", "│    2│", "└─────┘"],
        3: ["┌─────┐", "│3    │", "       ", "│    3│", "└─────┘"],
        4: ["┌─────┐", "│4    │", "       ", "│    4│", "└─────┘"],
        5: ["┌─────┐", "│5    │", "       ", "│    5│", "└─────┘"],
        6: ["┌─────┐", "│6    │", "       ", "│    6│", "└─────┘"],
        7: ["┌─────┐", "│7    │", "       ", "│    7│", "└─────┘"],
        8: ["┌─────┐", "│8    │", "       ", "│    8│", "└─────┘"],
        9: ["┌─────┐", "│9    │", "       ", "│    9│", "└─────┘"],
        10: ["┌─────┐", "│10   │", "       ", "│   10│", "└─────┘"],
        11: ["┌─────┐", "│J    │", "       ", "│    J│", "└─────┘"],
        12: ["┌─────┐", "│Q    │", "       ", "│    Q│", "└─────┘"],
        13: ["┌─────┐", "│K    │", "       ", "│    K│", "└─────┘"],
        14: ["┌─────┐", "│A    │", "       ", "│    A│", "└─────┘"]
    }

    display_card = ""
    for row in range(len(rank_art[2])):

        if row != 2:
            for element in card_list:
                display_card += rank_art[element.rank.value][row]

        else:
            for element in card_list:
                display_card += suit_art[element.suit.value]

        display_card += "\n"

    for index in range(len(card_list)):
        if index < 10:
            display_card += f"   {index}   "
        else:
            display_card += f"  {index}   "

    return display_card


class Hearts:

    def __init__(self) -> None:
        global round
        round = 1
        self.target_score = int_input("Please enter a target score to end the game: ")
        self.player_number = int_input("Please enter the number of players (3-5): ")
        self.valid_player_number()
        self.players = self.players_list()
        self.deck = self.deck()

        self.main()

    def main(self):
        global round
        game_end = False

        while game_end is False:
            self.start_round()
            self.end_round()
            round += 1
            game_end = self.check_game_end()

        self.display_winner()

    def valid_player_number(self):
        valid_player_number = False

        while not valid_player_number:
            if 3 <= self.player_number <= 5:
                valid_player_number = True
            else:
                self.player_number = int_input("Please enter the number of players (3-5): ")

        return self.player_number

    def players_list(self):
        players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"),
                   BasicAIPlayer("Player 4"), BasicAIPlayer("Player 5")]

        for i in range(5 - self.player_number):
            players.pop()

        return players

    def deck(self):

        deck = []
        for eachsuit in Suit:
            for eachrank in Rank:
                deck.append(Card(eachrank, eachsuit))

        if self.player_number == 3:
            deck.remove(Card(Rank.Two, Suit.Diamonds))

        elif self.player_number == 5:
            deck.remove(Card(Rank.Two, Suit.Diamonds))
            deck.remove(Card(Rank.Two, Suit.Spades))

        return deck

    def player_hand(self):

        random.shuffle(self.deck)

        deck_count = 0
        while deck_count < len(self.deck):
            for player in self.players:
                player.hand.append(self.deck[deck_count])
                deck_count += 1

        for player in self.players:
            print(f"{player} was dealt \n{card_interface(player.hand)}")
            # print(f"{player} was dealt {player.hand}")

    def pass_hand(self):
        pass_card_list = []
        for player in self.players:
            pass_card_list.append(player.pass_cards())

        index_list = []
        for i in range(round % len(self.players), len(self.players)):  # from index == round to end
            self.players[i].hand += pass_card_list[i - (round % len(self.players))]  # concatenate list
            # algorithm: index minus round(modulo with len(player))
            index_list.append(i - (round % len(self.players)))

        pass_card_reverse_index = 1
        # print()
        for i in range((round % len(self.players) - 1), -1, -1):
            # remaining players before index that haven't swapped hands (in reverse)
            self.players[i].hand += pass_card_list[len(pass_card_list) - pass_card_reverse_index]  # concatenate list
            # append remaining from last element

            index_list.insert(0, (len(pass_card_list) - pass_card_reverse_index))

            pass_card_reverse_index += 1

        for i in range(len(self.players)):
            print(f"{self.players[i]} passed to {self.players[index_list.index(i)]} \n{card_interface(pass_card_list[i])}")
            # print(f"{self.players[i]} passed {pass_card_list[i]} to {self.players[index_list.index(i)]}")
            # passing player of index of target in index_list

    def start_round(self):
        print(f"========= Starting round {round} =========")
        self.player_hand()
        if round % len(self.players) != 0:
            self.pass_hand()

        Round(self.players)

    def shot_the_moon(self):
        shot_the_moon = False

        for player in self.players:
            if player.round_score == 26:
                shot_the_moon = True
                print(f"{player} has shot the mooon! Everyone else receives 26 points")

        if shot_the_moon:
            for player in self.players:
                if player.round_score == 0:
                    player.round_score = 26
                elif player.round_score == 26:
                    player.round_score = 0

    def display_total_score(self):
        for player in self.players:
            player.total_score += player.round_score
            player.round_score = 0
            print(f"{player}'s total score: {player.total_score}")

    def check_game_end(self):
        check_game_end = False
        total_score_list = []
        for player in self.players:
            total_score_list.append(player.total_score)
            if player.total_score >= self.target_score:
                check_game_end = True

        winner_count = total_score_list.count(min(total_score_list))

        if winner_count != 1:
            check_game_end = False

        return check_game_end

    def end_round(self):
        print(f"========= End of round {round} =========")
        self.shot_the_moon()
        self.display_total_score()

    def display_winner(self):
        winning_player = self.players[0]
        for player in self.players:
            if player.total_score < winning_player.total_score:
                winning_player = player

        print(f"{winning_player} is the winner!")


Hearts()
