from time import sleep
while True:
    try:
        char_name=str(input("Please enter your character's name."))
        sword_name=str(input("Please enter your longsword's name."))
        vil_name=str(input("Please enter the village's name."))
        love_name=str(input("Enter your love's name."))
        love_action=str(input("Enter what you wish you had done to your love before leaving her."))
        break
    except ValueError:
        print("Please enter some text!")
        continue
print("%s Stood firm, brandishing his flaming longsword %s in one hand, and his templar's shield in the other. opposite him, a horde of demons, as dark and twisted as the other.calmly he reminisces of his time at home, the village of %s where hegrew up. He thinks of his love, %s, ashamed he hadn't %s her one last time before leaving."%(char_name,sword_name,vil_name,love_name,love_action))