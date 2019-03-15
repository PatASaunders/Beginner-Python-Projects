import string
import random
word_to_guess=["apple","jacuzzi","widow","matriarch","kingdom","axolotl","pioneer","nautilus","procrastination"]
letters=list(string.ascii_lowercase)
chosen=random.choice(word_to_guess)
print(chosen)
count=0
length=len(chosen)
guess_dump=[None]
while count!=12:
    try:
        guess=str(input("Please enter a letter!"))
    except ValueError:
        print("Please enter a basic letter of the alphabet")
        continue
    guess=guess.lower()
    if guess in guess_dump:
        print("You have already guessed this letter")
        continue
    guess_dump.append(guess)
    if guess in chosen:
        print("you guessed correctly!")
        print(str.replace(chosen, str in [guess_dump],"."))
        continue
    else:
        count=count+1
        print("wrong guess!")
        print("you have "+str(12-count)+" tries left")
print("you have either won or failed")