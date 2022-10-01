from __future__ import annotations
from basic_ai import BasicAIPlayer
from task3 import Round
from cards import Card, Rank, Suit
import random


class Hearts:

    def __init__(self) -> None:
        """
        Magic method that initializes the instance variables of the Hearts class with predefined values or user
        inputs (with validation tests) and executes the main method.
        """
        self.round = 1
        self.target_score = int_input("Please enter a target score to end the game: ")
        self.player_number = int_input("Please enter the number of players (3-5): ")
        self.valid_player_number()
        self.players = self.players_list()
        self.deck = self.deck()

        self.main()

    def main(self):
        """
        Method that executes multiple rounds until a player reaches the game's target score and there is only one
        winner.
        """
        game_end = False

        while game_end is False:
            self.start_round()
            self.end_round()
            self.round += 1
            game_end = self.check_game_end()

        self.display_winner()

        # Repeats until game_end is true, increments round by one after each start round and end round method execution
        # and updates the value of game_end by using the check_game_end method.

    def valid_player_number(self) -> int:
        """
        Method that verifies the user's input for the number of players and loops until a valid player number,
        which must be an integer between 3 and 5 (inclusive), is entered.
        """
        valid_player_number = False

        while not valid_player_number:
            if 3 <= self.player_number <= 5:
                valid_player_number = True
            else:
                self.player_number = int_input("Please enter the number of players (3-5): ")

        return self.player_number

        # Repeats until player_number is an integer between 3 and 5 (inclusive). Request additional input from the
        # user if player number is not an integer between 3 and 5 (inclusive). Finally, a valid player number is
        # returned.

    def players_list(self) -> list[Player]:
        """
        Method that produces and returns a list of Player objects based on the user-inputted number of players in the
        game.
        """
        players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"),
                   BasicAIPlayer("Player 4"), BasicAIPlayer("Player 5")]

        for n in range(5 - self.player_number):
            players.pop()

        return players

        # The game can only be played by a maximum of five players, therefore an initial list of players includes
        # five BasicAIPlayers. The abundance of BasicAIPlayers is then removed from the list of players based on the
        # user-inputted number of players.

    def deck(self):
        """
        Method that generates and returns a list of 52 distinct Card Objects based on a realistic deck, removing the
        Two of Diamonds if there are only three players and removing an extra Two of Spades if there are five players.
        """
        deck = []

        for each_suit in Suit:
            for each_rank in Rank:
                deck.append(Card(each_rank, each_suit))

        # Append the Card object to the deck list by looping over each card in the deck of every rank in each suit.

        if self.player_number == 3:
            deck.remove(Card(Rank.Two, Suit.Diamonds))

        # Remove the Two of Diamonds from the deck list if there are three players in the game

        elif self.player_number == 5:
            deck.remove(Card(Rank.Two, Suit.Diamonds))
            deck.remove(Card(Rank.Two, Suit.Spades))

        # Remove the Two of Diamonds and Two of Spades from the deck list if there are five players in the game

        return deck

    def start_round(self):
        """
        Method that displays the starting round banner, executes the player_hand and pass_hand method, then invokes
        the Round class to carry out a round.
        """
        print(f"========= Starting round {self.round} =========")

        valid_deal = False

        while not valid_deal:
            invalid_deal = False

            self.player_hand()

            for player in self.players:
                player.hand.sort()

                if player.hand[0] == Card(Rank.Queen, Suit.Spades) and player.hand[1].suit != Suit.Spades:
                    invalid_deal = True

                elif player.hand[0].suit == Suit.Hearts:
                    invalid_deal = True

            if invalid_deal is True:
                for player in self.players:
                    player.hand.clear()
            else:
                valid_deal = True

        # In order to keep the game from being ruined, it is required that each player has at least one card that
        # isn't the Queen of Spades or from the Hearts suit.

        # While valid deal is False, players are first dealt a hand of cards from the deck. Their hands are then
        # sorted to determine whether the Queen of Spades or a card from the Hearts suit is the first card (smallest
        # card) they have in their possession. If a player's first card is a Queen of Spades, the second card will be
        # checked to see if they have a bigger Spades card (a King of Spades or an Ace of Spades), and if they do not
        # (meaning they do not have at least one card that is not a Queen of Spades or a card from the Hearts suit),
        # invalid deal will be updated to True and all of the players' hands will be cleared off so that new cards
        # can be dealt to the players. Otherwise, valid deal will be updated to True, indicating that every player's
        # hand is valid.

        if self.round % len(self.players) != 0:
            self.pass_hand()

        # Players will not be required to pass cards in rounds that are multiples of the number of players in the game.

        Round(self.players)

    def player_hand(self):
        """
        Method that evenly distributes a hand of cards to each player after shuffling the deck of cards
        """
        random.shuffle(self.deck)

        # Randomly shuffle the deck of cards

        deck_count = 0

        while deck_count < len(self.deck):

            for player in self.players:
                player.hand.append(self.deck[deck_count])
                deck_count += 1

        # Deal a card to each player in the game, then do it again and again until the total number of dealt cards
        # equals the total number of cards in the deck list.

        for player in self.players:
            print(f"{player} was dealt {player.hand}")

    def pass_hand(self):
        """
        Algorithm-based method that enables players to pass their hands to other players in accordance with the
        game's round.
        """
        pass_card_list = []

        for player in self.players:
            pass_card_list.append(player.pass_cards())

        pass_order = []

        for index in range(self.player_number):
            if index + (self.round % self.player_number) >= self.player_number:
                pass_order.append(index + (self.round % self.player_number) - self.player_number)

            else:
                pass_order.append(index + (self.round % self.player_number))

        # For example, if there are four players and it is round one or round five, Player 1 will pass to Player 2,
        # Player 2 will pass to Player 3, Player 3 will pass to Player 4, and Player 4 will pass to Player 1. To
        # arrange the pass hand order for each player, a list variable called pass_order is initialised, and for the
        # example above, the list will generate to be [1, 2, 3, 0], where the index of the list corresponds to the
        # passer's index in the players list, and the elements of the list correspond to the retriever's index in the
        # players list.

        # The pass order list will be appended with an entry whose index is the index added with
        # (round % player number) using a for range loop that runs from index zero to the number of players in the
        # game. The element's value will be deducted by player number before being appended to the pass order list if
        # it is more than the total number of players in the game.

        for index in range(self.player_number):
            self.players[index].hand += pass_card_list[pass_order.index(index)]

        # Each player's hand is concatenated with their respective passed card using a for range loop starting at
        # index zero and going up to the number of players in the game. To do this, find each player's player index
        # in the players list in the pass_order list and use that value as the index to find their passed card in the
        # pass_card_list.

        for index in range(self.player_number):
            print(f"{self.players[index]} passed {pass_card_list[index]} to {self.players[pass_order[index]]}")

        # Display passing of cards of a player in terms of their passed card and to whom they passed to by using the
        # for loop index in the players list, pass_card_list, and pass_order_list.

    def end_round(self):
        """
        Method that displays the end round banner, and executes the shot_the_moon and display_total_score method.
        """
        print(f"========= End of round {self.round} =========")
        self.shot_the_moon()
        self.display_total_score()

    def shot_the_moon(self):
        """
        Method that checks if a player has shot the moon and, if so, changes each player's round score accordingly.
        """
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

        # Check if anyone in the game received a round score of 26 by looping over all players. The variable
        # shot_the_moon will be updated to True if a player receives a round score of 26, and that player's round
        # score will be updated to 0 while all other players receive a round score of 26.

    def display_total_score(self):
        """
        Method that displays each player's total score at the end of a round.
        """
        for player in self.players:
            player.total_score += player.round_score
            player.round_score = 0
            print(f"{player}'s total score: {player.total_score}")

        # Each player's round score is added to their total score by looping over all of the players in the game. The
        # total score is then printed, and the round score is then reset to zero.

    def check_game_end(self):
        """
        Method that determines whether the game has ended By determining if a player has reached the target score in
        terms of their total score and there is only one winner (meaning only one player with the smallest total score).
        """
        check_game_end = False
        total_score_list = []

        for player in self.players:
            total_score_list.append(player.total_score)
            if player.total_score >= self.target_score:
                check_game_end = True

        # For the purpose of checking for multiple winners, loop through every player in the game and add their total
        # score to total_score_list; if a player's total score exceeds the target score, check_game_end is updated to
        # be True.

        winner_count = total_score_list.count(min(total_score_list))

        if winner_count != 1:
            check_game_end = False

        # The variable check_game_end is set to be False and the game will continue if the number of minimum total
        # scores in total_score_list is more than one (signifying that there are multiple winners).

        return check_game_end

    def display_winner(self):
        """
        Method that identifies and displays the winning player, who is the player with the fewest total score after
        the game ends.
        """
        winning_player = self.players[0]

        for player in self.players:
            if player.total_score < winning_player.total_score:
                winning_player = player

        print(f"{winning_player} is the winner!")

        # Make the first player in the players list the temporary winning_player who will be used to make comparisons
        # in a for loop. The player whose score is lower than the winning_player's will subsequently be designated as
        # the new winning_player by looping through all of the game's players.


def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method, and keeps asking for input until a valid one is entered.
    Input can also be restricted to a set of integers.

    Arguments:
      - prompt: String representing the message to display for input
      - restricted: List of integers for when the input must be restricted to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)

        try:
            int_player_input = int(player_input)

        except ValueError:
            continue

        if restricted_to is None:
            break

        elif int_player_input in restricted_to:
            break

    return int_player_input


Hearts()
