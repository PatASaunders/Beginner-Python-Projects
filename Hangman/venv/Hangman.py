import string
import random
word_to_guess=["apple","jacuzzi","widow","matriarch","kingdom","axolotl","pioneer"]
letters=list(string.ascii_lowercase)
chosen=list(random.choice(word_to_guess))
print(chosen)
