import random
answer=str(input("Press y to play a guessing game!"))
while answer!="y":
    answer=str(input("Are you sure you don't want to play by pressing y?"))
print("A random number between 1 and 100 has been generated")
ran_num=random.randrange(1,100,)
print(ran_num)
while True:
    try:
        guess = int(input("Enter your guess!"))
    except ValueError:
        print("This is not a number!")
        continue
    if int(guess)<1 or int(guess)>100:
        print("The number has to be between 1 and 100!")
        continue
    elif ran_num==int(guess):
        print("Congratulations! You have guessed correctly.")
        break
    elif abs(ran_num-int(guess))<=5:
        print("Boiling!")
        continue
    elif abs(ran_num-int(guess))<=10:
        print("Hot!")
        continue
    elif abs(ran_num-int(guess))<=20:
        print("Lukewarm.")
        continue
    else:
        print("Freezing!")
        continue