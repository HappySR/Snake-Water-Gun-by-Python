'''
Snake = "s"
Water = "w"
Gun = "g"
'''
import random

dict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}
revdict = {
    1 : "Snake",
    -1 : "Water",
    0 : "Gun"
}

comp = random.choice([1,0,-1])
user = input("Enter your choice : ")
you = dict[user]

print(f"You chose {revdict[you]}\nComputer chose {revdict[comp]}")

if(comp == you):
    print("Draw!")
elif((comp == 1 and you == 0) or (comp == 0 and you == -1) or (comp == -1 and you == 1)):
    print("You Win!")
else:
    print("You Lose!")