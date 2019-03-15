import random
elements = ["rock","paper","scissors"]
player_choice_1=None
player_choice_2=None
while True:
    try:
        num_players = int(input("Please indicate the number of players between 1 and 2."))
        if num_players == 1 or 2:
           break
        else:
            continue
    except ValueError:
        continue
if num_players == 1:
    print("You will play against the AI.")
    print("You may type 'Stop' to stop the game at any time.")
    while player_choice_1 != "Stop":
        while True:
            try:
                player_choice_1 = str(input("Please type: 'rock', 'paper', or 'scissors'."))
                if player_choice_1=="rock" or "paper" or "scissors":
                    break
            except ValueError:
                print("Please type: 'rock', 'paper', or 'scissors'.")
                continue
        ai_choice=random.choice(elements)
        if elements.index(ai_choice)==2 and elements.index(player_choice_1)==0:
            print(str(player_choice_1) + " beats " + str(ai_choice) + ", you win!")
        elif elements.index(ai_choice)==elements.index(player_choice_1)-1:
            print(str(player_choice_1) + " beats " + str(ai_choice) + ", you win!")
        elif elements.index(ai_choice)==elements.index(player_choice_1):
            print("You have both chosen " + str(player_choice_1) + "!")
        else:
            print(str(ai_choice) + " beats " + str(player_choice_1) + ", you lose!")
if num_players == 2:
    print("Please assign player 1 and player 2 between yourselves.")
    print("You may type 'Stop' to stop the game at any time.")
    while player_choice_1 != "Stop" or player_choice_2 != "Stop":
        while True:
            try:
                player_choice_1 = str(input("Player 1, please type: 'rock', 'paper', or 'scissors'."))
                if player_choice_1=="rock" or "paper" or "scissors":
                    break
            except ValueError:
                continue
        while True:
            try:
                player_choice_2 = str(input("Player 2, please type: 'rock', 'paper', or 'scissors'."))
                if player_choice_1=="rock" or "paper" or "scissors":
                    break
            except ValueError:
                continue
        if elements.index(player_choice_2)==2 and elements.index(player_choice_1)==0:
            print(str(player_choice_1) + " beats " + str(player_choice_2) + "!")
        elif elements.index(player_choice_2)==elements.index(player_choice_1)-1:
            print(str(player_choice_1) + " beats " + str(player_choice_2) + "!")
        elif elements.index(player_choice_2)==elements.index(player_choice_1):
            print("You have both chosen " + str(player_choice_1) + "!")
        else:
            print(str(player_choice_2) + " beats " + str(player_choice_1) + "!")