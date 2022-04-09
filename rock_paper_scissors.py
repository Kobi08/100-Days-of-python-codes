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

game_image = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

random_cp_choice = random.randint(0, 2)
print(f"Computer Choice {game_image[random_cp_choice]}")

if player_choice >= 3 or player_choice < 0:
  print("You type invalid number, you lose")
elif player_choice == 0 and random_cp_choice == 2:
  print("You Win")
elif random_cp_choice == 0 and player_choice == 2:
  print("You Lose")
elif random_cp_choice > player_choice:
  print("You Lose")
elif player_choice > random_cp_choice:
  print("You Win")
elif random_cp_choice == player_choice:
  print("It's a draw")
 