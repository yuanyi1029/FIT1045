from __future__ import annotations
from cards import Card, Rank, Suit
import time


class Round:

    def __init__(self, players: list[Player]) -> None:
        """
        Magic method that initializes the instance variables of the Round class and executes the main method.

        Arguments:
            -players: List of Player objects that are in the game
        """
        self.players = players
        self.broken_hearts = False

        self.main()

    def main(self):
        """
        Method that executes a round of multiple tricks until all the cards are played from each player's hand.
        """
        leader = self.first_leader()

        while len(self.players[0].hand) != 0:
            leader = self.taker(leader, self.execute_round(leader))

        # Assign the player having the Two of Clubs in hand as the first leader of a trick.
        # After each execute_round, designate a new leader to the round taker, and repeat until each player's hands are
        # empty.

    def execute_round(self, leader: Player) -> list[Card]:
        """
        Method that enables every player in the players list to play a card from their hand and updates the broken
        hearts variable to true if a Hearts card is played for the first time.

        Arguments
            -leader: Player object that will start the trick
        """
        trick = []
        turn_count = 0

        for player in self.turn_order(leader):
            time.sleep(1)
            played_card = player.play_card(trick, self.broken_hearts)

            if turn_count == 0:
                print(f"{player} leads with {card_interface(played_card)}")

            else:
                print(f"{player} plays {card_interface(played_card)}")

            if self.broken_hearts is False:

                if played_card.suit == Suit.Hearts:
                    self.broken_hearts = True
                    print("Hearts have been broken!")

            trick.append(played_card)
            turn_count += 1
            time.sleep(1)

        return trick

        # Allows each player on the turn order list to play a card, checks to see whether hearts are broken, and appends
        # each card played to the trick list.

    def first_leader(self) -> Player:
        """
        Method used to determine player who would lead the opening trick of the round.
        """
        for player in self.players:
            player.hand.sort()

            if player.hand[0] == Card(Rank.Two, Suit.Clubs):
                return player

        # The person who has the Two of Clubs in their hand is returned after going through every player in game,
        # sorting their hands in ascending order, and checking their first card in hand to see whether it is the Two
        # of Clubs because it is the smallest card in the deck.

    def turn_order(self, leader: Player) -> list[Player]:
        """
        Method that takes in a trick's leader as an argument and arranges the play order of the trick to adhere to the
        leader.

        Arguments
            -leader: Player object that will start the trick
        """
        turn_order = []

        for i in range(self.players.index(leader), len(self.players)):
            turn_order.append(self.players[i])

        for i in range(self.players.index(leader)):
            turn_order.append(self.players[i])

        return turn_order

        # Arranges turn order by first appending players to the turn_order list, from the leader to the last player
        # on the players list. The remaining players are then added to the turn order list, starting with the first
        # player in the players list (inclusive) and ending with the leader (non-inclusive).

    def taker(self, leader: Player, trick: list[Card]) -> Player:
        """
        Method that determines which player will take the trick, decides how many penalty points they will get,
        and updates their round score.

        Arguments
            -leader: Player object that will start the trick
            -trick: List of Card objects in the trick
        """
        taker_played_card = trick[0]

        for card in trick:
            if card.suit == taker_played_card.suit and card.rank > taker_played_card.rank:
                taker_played_card = card

        taker = self.turn_order(leader)[trick.index(taker_played_card)]

        # Determine the taker by searching for cards that have the same suit as the trick's opening card,
        # then see which card has the higher rank. The player at that index of the turn_order list is then determined
        # as the taker by using the index of the taker_played_card in the trick list.

        penalty = 0

        for card in trick:
            if card.suit == Suit.Hearts:
                penalty += 1

            elif card == Card(Rank.Queen, Suit.Spades):
                penalty += 13

        print(f"{taker} takes the trick. Points received: {penalty}")

        self.players[self.players.index(taker)].round_score += penalty

        # The total penalty points are calculated by looping over each card in the trick list, with the Hearts Card
        # having one point and the Queen of Spades having thirteen. Following that, the penalty points are added to
        # the taker's round score.

        return taker


def card_interface(card: Card) -> str:
    """
    Helper function that accepts a Card object that was played by a player and returns the card as a string art
    displaying the played card interface

    Arguments:
        - card: Card Objects that was played

    Returns the card that was played by a player as a string art displaying the played card interface in string type.
    """
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
        display_card += "\n"
        if row != 2:
            display_card += rank_art[card.rank.value][row]

        else:
            display_card += suit_art[card.suit.value]

    # Repeat this process until there are a total of five rows (following the length of one of the keys in rank art,
    # in this instance key: 2), which is necessary to print a card's art from top to bottom. Then, using matching
    # rank art and suit art to the card, display_card is concatenated from left to right to display each row.

    return display_card




