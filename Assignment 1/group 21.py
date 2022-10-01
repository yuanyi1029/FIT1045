"""
Group name: 7-11
Authors: Yee Khai Wei, Wong Yuan Yi, Tong Zhi Enn, Cheong Jia Yang
"""

import time
import random
import os


def display_rules():
    print("""
  _____________________________________________________________________________
  Twenty One is a game of chance where players take turns rolling two dice every 
  round until they decide to stop rolling and lock in their score or end up 
  going bust with a total over 21. The objective is to be the closest to 21 
  when everyone is done rolling.

  Rules are as per follows:
    - Players begin with a score of 0.
    - Each player has one turn to either roll or stop rolling each round.
    - Players can only do a regular roll of two dice until they 
      reach a score of at least 14.
    - Players with a score >= 14 have the option to only roll one dice.
    - If a player scores more than 21 they go bust and are out of the game.
    - The winning player is the one with the score closest to 21 when everyone 
      has finished rolling.
    - If all players go bust, no one wins.
    - If more than one player has the winning score, no one wins.
  _____________________________________________________________________________
  """)
    input("Press enter to go back")
    return


def display_main_menu():
    print("------------Main Menu------------")
    print("Welcome to Twenty One!")
    print("1. Solo")
    print("2. Local Multiplayer")
    print("3. Rules")
    print("4. Exit")
    print("---------------------------------")


def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input
    can also be restricted to a set of integers.-

    Arguments:
      - prompt: String representing the message to display for input
      - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

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


def cpu_player_choice(score: int) -> int:
    """
    This function simply returns a choice for the CPU player based
    on their score.

    Arguments:
      - score: Int

    Returns an int representing a choice from 1, 2 or 3.
    """
    time.sleep(1.5)  # time taken for CPU Player to response
    if score < 14:
        return 1
    elif score < 17:
        return 3
    else:
        return 2


def display_game_options(player: dict):
    """
    Prints the game options depending on if a player's score is
    >= 14.

    Arguments:
      - player: A player dictionary object
    """
    print("------------" + player["name"] + "'s turn------------")
    # reveals the player's turn by taking the player's name from the player dictionary
    print(player["name"] + "'s score:", player["score"])
    # reveals the player's score by taking the player's name and score from the player dictionary
    print("1. Roll")  # player rolls two dice
    print("2. Stay")  # player stays for the round

    if player["at_14"] is True:  # if the player's score is at least 14, display the third option: Roll one
        print("3. Roll One")  # player rolls for a dice


def display_round_stats(round: int, players: list):
    """
    Print the round statistics provided a list of players.

    Arguments:
      - round: Integer for round number
      - players: A list of player-dictionary objects
    """
    print("-----------Round", str(round) + "-----------")  # shows the number of rounds after every turns

    for i in players:
        # reveals each player's score by taking the player's name and score from the player dictionary using for loop
        print(i["name"], "is at", i["score"])


def roll_dice(num_of_dice=1):
    """
    Rolls dice based on num_of_dice passed as an argument.

    Arguments:
      - num_of_dice: Integer for amount of dice to roll

    Returns the following tuple: (rolls, display_string)
      - rolls: A list of each roll result as an int
      - display_string: A string combining the dice art for all rolls into one string
    """
    rolls = []
    display_string = ""

    for i in range(num_of_dice):  # randomise a number from 1 to 6 according to the num_of_dice for the loop
        rolls.append(random.randint(1, 6))  # append each randomly generated number from 1 to into rolls

    die_art = {    
        1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
        2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
        3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
        4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
        5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
        6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }

    for n in range(5):  # repeat until there are five rows total, which is required to print a dice from top to bottom
        # five elements in a dictionary, then go throuh rolls and concat the top of the to each other
        for i in range(len(rolls)):  # repeat for each element in rolls
            # die_art is concatenated from left to right to build each row using matching die_art and elements in rolls
            if rolls[i] == 1:
                display_string += die_art[1][n]
            elif rolls[i] == 2:
                display_string += die_art[2][n]
            elif rolls[i] == 3:
                display_string += die_art[3][n]
            elif rolls[i] == 4:
                display_string += die_art[4][n]
            elif rolls[i] == 5:
                display_string += die_art[5][n]
            elif rolls[i] == 6:
                display_string += die_art[6][n]

        display_string += "\n"  # prints a new line after concatenating a row

    return rolls, display_string
    

def execute_turn(player, player_input):
    """
    Executes one turn of the round for a given player.

    Arguments:
      - player: A player dictionary object

    Returns an updated player dictionary object.
    """
    if player_input == 1:  # roll two dice if a player inputs one, then results is added into the score
        print("Rolling both...")
        results = roll_dice(2)  # this line rolls two dice
        print(results[1]) # prints die_art
        player["score"] += sum(results[0])  # updates player score
        print(player["name"], "is now on", player["score"])

    elif player_input == 2:  # if a player inputs two, updates "stayed" in dictionary to true and displays final score
        print(player["name"], "has stayed with a score of", player["score"])
        player["stayed"] = True

    elif player_input == 3:  # roll one dice if a player inputs three, then add the results to the score
        print("Rolling one...")
        results = roll_dice(1)  # this line rolls one dice
        print(results[1]) # prints die_art
        player["score"] += sum(results[0]) # updates player score
        print(player["name"], "is now on", player["score"])

    if player["score"] >= 14:  # if player score is >= 14, updates "at_14" in dictionary to true
        player["at_14"] = True

        if player["score"] > 21:  # if player score is > 21, updates "bust" in dictionary to true
            player["bust"] = True

    return player


def end_of_game(players):
    """
    Takes the list of all players and determines if the game has finished,
    returning false if not else printing the result before returning true.

    Arguments:
      - players: A list of player-dictionary objects

    Returns True if round has ended or False if not. If true results are
    printed before return.
    """
    winner = None
    winner_score = 0
    draw = False

    for i in range(len(players)):  # repeat for the number of players playing
        if players[i]["score"] == winner_score:  # if a player's score matches the winner_score, draw will be true
            draw = True

        elif 21 >= players[i]["score"] > winner_score:  # if a player's score is <= 21 and > winner_score,
            winner = players[i]["name"]  # updates winner to player's name
            winner_score = players[i]["score"]  # updates winner_score to player's score
            draw = False

    for i in range(len(players)):  # repeat for the number of players playing
        if players[i]["score"] < 21 and players[i]["stayed"] is False:
            return False

    if draw:
        print("The game is a draw! No one wins :(")

    elif winner is None:
        print("Everyone's gone bust! No one wins :(")

    else:
        print(winner, "is the winner!")

    return True


def validate_player_input(players, player_in_turn):
    valid_player_input = False
    # verify the player's input to see if it is valid

    while not valid_player_input:  # repeat until a valid option is entered
        player_input = int_input("Please enter an option: ")

        if player_input == 3:  # verify whether the player's "at 14" is true if three is entered

            if players[player_in_turn]["at_14"]:  # valid_player_input becomes true if "at 14" is true
                valid_player_input = True

            else:
                print("Invalid input!")

        elif player_input == 1 or player_input == 2:
            valid_player_input = True

        else:  # if the entered option is not one, two, or three, the input is invalid
            print("Invalid input!")

    return player_input


def solo_game():
    """
    This function defines a game loop for a solo game of Twenty One against
    AI.
    """
    players = [{"name": "Player 1", "score": 0, "stayed": False, "at_14": False, "bust": False},
               {"name": "CPU Player", "score": 0, "stayed": False, "at_14": False, "bust": False}]

    round = 0

    while end_of_game(players) is False:  # repeat until end_of_game is true
        print()

        display_round_stats(round, players)

        for player_in_turn in range(len(players)):
            # index returned from length of players list using for loops determines which player turn it is
            print()
            if players[player_in_turn]["bust"] is False and players[player_in_turn]["stayed"] is False:
                # turn will be skipped if a player busted or stayed
                display_game_options(players[player_in_turn])  # game option will also be determined by players' turn

                if player_in_turn == 0:
                    player_input = validate_player_input(players, player_in_turn)
                else:
                    player_input = cpu_player_choice(players[1]["score"])
                    # providing the CPU score to the cpu_player_choice function to get CPU's input

                execute_turn(players[player_in_turn], player_input)

                if players[player_in_turn]["score"] > 21:
                    # if a player's score is > 21, indicate that the player busted
                    print(players[player_in_turn]["name"], "goes bust!")

                time.sleep(1)

            elif players[player_in_turn]["bust"] is True:  # if a player busted, print a message to skip the turn
                print(players[player_in_turn]["name"], "busted! Skipping turn...")

            elif players[player_in_turn]["stayed"] is True:  # if a player stayed, print a message to skip the turn
                print(players[player_in_turn]["name"], "stayed! Skipping turn...")

            time.sleep(1)

        round += 1
        print("\n")


def multiplayer_game(num_of_players):
    """
    This function defines a game loop for a local multiplayer game of Twenty One,
    where each iteration of the while loop is a round within the game.
    """

    def player_info():  # function to gather player's information (name)
        player = {"name": input("Name: "), "score": 0, "stayed": False, "at_14": False, "bust": False}
        return player

    players = []
    for number in range(num_of_players):  # repeat for num_of_player
        print("Player", number + 1)
        players.append(player_info())  # input player's information (name) into players list

    round = 0

    while end_of_game(players) is False:  # repeat until end_of_game is true
        print()

        display_round_stats(round, players)

        for player_in_turn in range(len(players)):
            # index returned from length of players list using for loops determines which player turn it is
            print()
            if players[player_in_turn]["bust"] is False and players[player_in_turn]["stayed"] is False:
                # turn will be skipped if a player busted or stayed
                display_game_options(players[player_in_turn])  # game option will also be determined by players' turn

                player_input = validate_player_input(players, player_in_turn)

                execute_turn(players[player_in_turn], player_input)

                if players[player_in_turn]["score"] > 21:
                    # if a player's score is > 21, indicate that the player busted
                    print(players[player_in_turn]["name"], "goes bust!")

                time.sleep(1)

            elif players[player_in_turn]["bust"] is True:  # if a player busted, print a message to skip the turn
                print(players[player_in_turn]["name"], "busted! Skipping turn...")

            elif players[player_in_turn]["stayed"] is True:  # if a player stayed, print a message to skip the turn
                print(players[player_in_turn]["name"], "stayed! Skipping turn...")

            time.sleep(1)

        round += 1
        print("\n")


def main():
    """
    Defines the main loop that allows the player to start a game, view rules or quit.
    """
    while True:
        os.system("clear")  # every time a new game begins, clear the terminal
        display_main_menu()  # a main menu will appear to allow user to pic their choices
        menu_option = int_input("Please enter an option: ")  # allows user to enter their input

        if menu_option == 1:  # when option 1 is picked, it will bring the user to enter solo game
            solo_game()

            input("\nPress enter to go back")

        elif menu_option == 2:  # when option 2 is picked, it will bring the user to enter multiplayer game
            valid_num_of_players = False
            # verify the player's input to see if it is valid

            while not valid_num_of_players:  # repeat until a valid option is entered
                num_of_players = int_input("Enter number of players: ")

                if num_of_players > 1:
                    # only takes input higher than one, as multiplayer games demand a minimum of two players
                    valid_num_of_players = True

                else:
                    print("Invalid input! A multiplayer game requires at least two players to be played!")

            multiplayer_game(num_of_players)

            input("\nPress enter to go back")

        elif menu_option == 3:  # shows user the rules of the game  when user enters option 3
            display_rules()

        elif menu_option == 4:  # exits the game when user enters option 4
            print("Exiting Twenty One...")
            break  # stop infinite loop

        else:  # if the entered option is not one, two, three, or four, the input is invalid
            print("Invalid input!")


main()  # calls main procedure to start the application

# Additional Features:
# Each new game clears the terminal.
# A player's name can be entered for multiplayer games.
# There are only three possible inputs for execute turn, and input 3 will only be accepted if at 14 is true.
# Multiplayer input validation only allows for more than 1 players.