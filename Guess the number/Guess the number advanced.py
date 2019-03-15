import random
answer=str(input("Press y to play a guessing game!"))
while answer!="y":
    answer=str(input("Are you sure you don't want to play by pressing y?"))
print("A random number between 1 and 100 has been generated")
ran_num=random.randrange(1,100,)
count=1
guess=0
while True:
    guess_old=guess
    try:
        guess=int(input("Enter your guess!"))
    except ValueError:
        print("This is not a number!")
        continue
    if int(guess)<1 or int(guess)>100:
        print("The number has to be between 1 and 100!")
        continue
    elif ran_num==int(guess):
        print("Congratulations! You have guessed correctly.")
        break
    else:
        if count==1:
            ("Sorry your guess is wrong.")
            count=2
        elif abs(guess_old-ran_num)>abs(guess-ran_num):
            print("Warmer!")
        else:
            print("You are getting colder!")