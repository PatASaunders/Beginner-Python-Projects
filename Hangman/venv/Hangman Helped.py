import random
hangman = (

"""
.
""",
"""

----------
""",
"""
 |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-
 |  | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  |   |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  | | |
 |    |
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  | | |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  |-+-|
 |  | | |
 |    |
 |   | |
 |   | |
 |  
----------
""")
chosen=random.choice(["apple","jacuzzi","widow","matriarch","kingdom","axolotl","pioneer","nautilus","procrastination"])
count=0
ans=("-")*len(chosen)
char_dump=[]
print("Welcome!")
input("Press Enter to Start")
while count!=11 and ans!=chosen:
    print()
    print("Letters used so far: ",char_dump)
    print("Where we are so far: ",ans)
    guess=input("Guess a letter: ").lower()
    while guess in char_dump:
        print("you have already guessed this letter!")
        guess=input("Guess another letter: ").lower()
    char_dump.append(guess)
    if guess in chosen:
        new=""
        for i in range(len(chosen)):
            if guess == chosen[i]:
                new+=guess
            else:
                new+=ans[i]
        ans=new
    else:
        print("Sorry!")
        count+=1
    print(hangman[count])
if ans==chosen:
    print("You win!")
else:
    print("Sorry, you lost!")
