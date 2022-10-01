from __future__ import annotations
from cards import Card
from player import Player


class Human(Player):

    def __init__(self) -> None:
        """
        Magic method that initializes the instance variables of the Player Class (Parent class) with user input (name).
        """
        super().__init__(input("Please enter your name: "))

    def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
        """
        Method that enables the Human Player to play a card by inputting the appropriate card's index in their hand.

        Arguments:
            -trick: List of Card objects in the current trick
            -broken_hearts: Boolean value to represent if hearts have been broken
        """
        self.hand.sort()

        if len(trick) != 0:
            print(f"Current trick: {card_interface(trick, False)}")

        else:
            print(f"{self.name} leads the trick.")

        print(f"Your current hand: {card_interface(self.hand, True)}")

        # Displays the current trick and the player's current hand in a string art in order to let the player input
        # their desired play more easily.

        valid_play = False
        play = int_input("Select a card to play: ")

        while valid_play is False:
            if play < 0 or play >= len(self.hand):
                print(f"Input is not within the appropriate range of 0 to {len(self.hand) - 1}")
                play = int_input("Select a card to play: ")

            # Range check

            elif self.check_valid_play(self.hand[play], trick, broken_hearts)[0] is False:
                print(self.check_valid_play(self.hand[play], trick, broken_hearts)[1])
                play = int_input("Select a card to play: ")

            # Valid play check

            else:
                valid_play = True

        card = self.hand[play]
        self.hand.remove(card)
        return card

        # After the player plays a card that is valid, the card is removed from their hand and the card that was
        # played is returned.

    def pass_cards(self) -> list[Card]:
        """
        Method that enables the Human Player to pass three cards by inputting the appropriate cards' indexes in their
        hand.
        """
        self.hand.sort()

        print(f"Your current hand: {card_interface(self.hand, True)}")

        # Displays the player's current hand in a string art in order to let the player input their desired pass
        # cards more easily.

        valid_pass_off = False
        pass_off = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
        pass_off_list = pass_off.split(", ")

        while valid_pass_off is False:
            if len(pass_off_list) != 3:
                print("Three values must be entered and be separated by commas.")
                pass_off = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
                pass_off_list = pass_off.split(", ")

            # Format check

            elif list_is_integer(pass_off_list) is False:
                print("Entered values must be integers.")
                pass_off = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
                pass_off_list = pass_off.split(", ")

            # Type check

            elif len(set(pass_off_list)) != 3:
                print("Entered values must be distinct.")
                pass_off = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
                pass_off_list = pass_off.split(", ")

            # Distinct value check

            else:
                valid_pass_off = True
                for index in pass_off_list:
                    if int(index) < 0 or int(index) >= len(self.hand):
                        valid_pass_off = False

                if valid_pass_off is False:
                    print(f"Input is not within the appropriate range of 0 to {len(self.hand) - 1}")
                    pass_off = input("Select three cards to pass off (e.g. '0, 4, 5'): ")
                    pass_off_list = pass_off.split(", ")

            # Range check

        for index in range(len(pass_off_list)):
            pass_off_list[index] = int(pass_off_list[index])

        # Converts pass_off_list from a string list to an integer list.

        pass_off_list.sort()
        pass_off_list.reverse()

        pass_card_list = []
        for index in pass_off_list:
            pass_card_list.append(self.hand[int(index)])
            self.hand.remove(self.hand[int(index)])

        # As the length of the player's hand decreases with each removal of a pass card, sorting the pass off list in
        # descending order will allow the player to remove the biggest pass card from their hand first without
        # triggering an error since the other smaller pass cards' indices won't be affected when the player's hand
        # length shrinks after each removal of a bigger pass card.

        pass_card_list.sort()

        return pass_card_list


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


def list_is_integer(list_to_be_checked: list) -> bool:
    """
    Helper function that checks to see if each element in the list argument passed is an integer.

    Arguments:
    - list_to_be_checked: List where each element must be checked to see whether they are an integer.

    Returns if each element in the list is an integer in boolean type.
    """
    for element in list_to_be_checked:
        try:
            int(element)

        except ValueError:

            return False

    return True


def card_interface(card_list: list[Card], print_index: bool) -> str:
    """
    Helper function that accepts a list of Card objects that represent the player's hand and returns the list as a
    row of string art displaying the player's hand's card interface along with each card's index.

    Arguments:
        - card_list: List of Card Objects representing the player's hand
        - print_index: Boolean value to indicate whether or not the index of the card list needs to be printed.

    Returns the card list as a row of string art displaying the player's hand's card interface along with each card's
    index in string type.
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
            for element in card_list:
                display_card += rank_art[element.rank.value][row]

        else:
            for element in card_list:
                display_card += suit_art[element.suit.value]

    # Repeat this process until there are a total of five rows (following the length of one of the keys in rank art,
    # in this instance key: 2), which is necessary to print a card's art from top to bottom. Then, using matching
    # rank art and suit art to the element (card), display_card is concatenated from left to right for each element
    # (card) in the card list to display each row.

    if print_index:
        display_card += "\n"

        for index in range(len(card_list)):
            if index < 10:
                display_card += f"   {index}   "

            else:
                display_card += f"  {index}   "

    # Concatenated the index of the card in the card list underneath the display card when print index is true (when
    # the Human Player is choosing cards to pass and play from their hand).

    return display_card
