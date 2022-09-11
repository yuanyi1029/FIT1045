import time
import random

def main():
    while True:
        display_menu()
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            solo_game()
        elif menu_choice == 2:
            num_of_players = int(input("Please enter amount of players: "))
            multiplayer_game(num_of_players)
        elif menu_choice == 3:
            display_rules()
        elif menu_choice == 4:
            print("Quitting Game ...")
            break
    #   raise NotImplementedError

def display_rules():
    print("""
-------------------------------------------------------------------------------
Twenty One is a game of chance where players take turns rolling dice and 
tallying the results until they decide to stop rolling and lock in their score,
or end up going bust with a total over 21. The objective is to be the closest 
to 21 when everyone is done rolling.

- Players begin with a score of 0.
- Each player has one turn to either roll or stop rolling each round.
- Players can only do a regular roll of two dice until they 
  reach a score of at least 14.
- Players with a score >= 14 have the option to only roll one dice.
- If a player scores more than 21 they go bust and are out of the game.
- The winning player is the one with the score closest to 21 when everyone has 
  finished rolling.
- If all players go bust, no one wins.
- If more than one player has the winning score, no one wins.
-------------------------------------------------------------------------------""")
    input("Press any key to go back")
    #   raise NotImplementedError

def display_menu():
    print("""
------------Main Menu------------
Welcome to Twenty One!
1. Solo
2. Local Multiplayer
3. Rules
4. Exit
---------------------------------""")
    #   raise NotImplementedError

def multiplayer_game(num_of_players):
    players = []
    for t in range(1,num_of_players+1):
        players.append({'name': 'Player ' + str(t), 'score': 0, 'stayed': False, 'at_14': True, 'bust': False})
    current_round = 0

    while end_of_game(players) == False:
        for y in range(num_of_players):
            display_round_stats(current_round, players)       
            display_game_options(players[y])
            decision = int(input("Please enter an option: "))
            execute_turn(players[y], decision)
        current_round += 1 
    # raise NotImplementedError

def cpu_choice(player):
    time.sleep(2)
    if player['score'] < 14:
        return 1 
    elif player['score'] < 17:
        return 3
    else:
        return 2
    #   raise NotImplementedError

def solo_game():
    player = {'name': 'Player 1', 'score': 0, 'stayed': False, 'at_14': True, 'bust': False}
    cpu_player = {'name': 'CPU Player', 'score': 0, 'stayed': False, 'at_14': True, 'bust': False}
    players = [player, cpu_player]
    current_round = 0 

    while end_of_game(players) == False:
        display_round_stats(current_round, players)         # display round
        display_game_options(player)                        # display player 1 option
        decision = int(input("Please enter an option: "))   # ask for decision input (1/2/3)
        execute_turn(player, decision)                      # adds up player 1 points
        display_game_options(cpu_player)                    # display cpu option
        execute_turn(cpu_player, cpu_choice(cpu_player))    # adds up cpu points based on cpu decision
        current_round += 1 
    #   raise NotImplementedError

def display_game_options(player):
    print("------------"+ player['name']+"'s turn------------")
    print(player['name'] + "'s score: " + str(player['score']))
    print("1. Roll")
    print("2. Stay")
    if player['score'] >= 14:
        print("3. Roll One")
    # raise NotImplementedError

def display_round_stats(round, players):
    print("-----------Round " + str(round) + "-----------")
    for k in range (len(players)):
        print(players[k]['name'] + " is at " + str(players[k]['score']))
    # raise NotImplementedError

def roll_dice(num_of_dice=1):
    totalrolls = []
    die_art_display = ""
    die_art = {
        1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
        2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
        3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
        4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
        5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
        6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"]
    }

    for i in range (num_of_dice):
        eachroll = random.randint(1,6)
        totalrolls.append(eachroll)
    
    for x in range(5):
        for j in range(len(totalrolls)):
            if totalrolls[j] == 1:
                die_art_display += die_art[1][x]
            if totalrolls[j] == 2:
                die_art_display += die_art[2][x]
            if totalrolls[j] == 3:
                die_art_display += die_art[3][x]
            if totalrolls[j] == 4:
                die_art_display += die_art[4][x]
            if totalrolls[j] == 5:
                die_art_display += die_art[5][x]
            if totalrolls[j] == 6:
                die_art_display += die_art[6][x]

        die_art_display += "\n"
    return totalrolls, die_art_display
    # raise NotImplementedError

def execute_turn(player, player_input):
    if player_input == 1:
        print("Rolling both...")
        result = roll_dice(2)
        print(result[1])
        for c in result[0]:
            player['score'] += c
        print(player['name'] + " is now on " + str(player['score']))
    elif player_input == 2:
        print(player['name'] + " has stayed with a score of " + str(player['score']))
        player['stayed'] = True
    elif player_input == 3:
        print("Rolling one...")
        result = roll_dice(1)
        print(result[1])  
        for c in result[0]:
            player['score'] += c
        print(player['name'] + " is now on " + str(player['score']))
        
    if player['score'] >= 14:
        player['at_14'] = True
    if player['score'] > 21:
        player['bust'] = True
        print(player['name'] + " goes bust!")
    # raise NotImplementedError

def end_of_game(players):

    winner = ""
    winning_score = 0
    draw = False
    player_out = 0
    bust_players = 0

    for b in range (len(players)):
        if players[b]['score'] == winning_score:
            draw = True
        elif players[b]['score'] > winning_score and players[b]['score'] <= 21:    
            winner = players[b]['name']    
            winning_score = players[b]['score']
            draw = False


    for b in range (len(players)):
        if players[b]['score'] >= 21 or players[b]['stayed'] is True:
            player_out += 1
    if player_out == len(players):
        end_game = True
    else:
        end_game = False
    

    for b in range (len(players)):
        if players[b]['bust'] is True:
            bust_players += 1
    if bust_players == len(players):
        end_game = True


    if end_game is True:
        if draw == True:
            print("The game is a draw! No one wins :(") 
        elif bust_players == len(players):
            print("Everyone's gone bust! No one wins :(")
        else:
            print(winner + " is the winner!")
    
    return end_game
    # raise NotImplementedError

main()