rock = '''
    _______
---'   ____)
      (_____)
      (_____)                       
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game = [rock, paper,scissors ]
randomness = random.choice(game)
choice_rock_paper_scissors = input("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if choice_rock_paper_scissors == "0":
    print(rock)
    print("Computer chose: ", randomness)
    if randomness == rock:
        print("It's a tie.\nLet's play again.")
    elif randomness == paper:
        print("You Lose.\nLet's see if you can win this time.")
    elif randomness == scissors:
        print("You Win.\nLet's see if you can win again.")
elif choice_rock_paper_scissors == "1":
    print(paper)
    print("Computer chose: ", randomness)
    if randomness == rock:
        print("You Win.\nLet's see if you can win again.")
    elif randomness == paper:
        print("It's a tie.\nLet's play again.")
    elif randomness == scissors:
        print("You Lose.\nLet's see if you can win this time.")
elif choice_rock_paper_scissors == "2":
    print(scissors)
    print("Computer chose: ", randomness)
    if randomness == rock:
        print("You Lose.\nLet's see if you can win this time.")
    elif randomness == paper:
        print("You Win.\nLet's see if you can win again.")
    elif randomness == scissors:
        print("It's a tie.\nLet's play again.")
else :
    print("Invalid Choice\nYou Lose.")