import random

input("Press Enter to play Poker!")
players=[]
player_name=0
count=1
print("The minimum number of players is 2, the maximum is 6.")
while player_name!="Done" and count!=7:
    if count >= 2:
        print("Type 'Done' if you are finished.")
    player_name=input("Please enter the name of competitor number " + str(count) +":")
    players.append(player_name)
    count = count+1
print("Ok names are saved.")
print("Each player will receive 1500 dollars.")