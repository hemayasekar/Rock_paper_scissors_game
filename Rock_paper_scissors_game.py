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

img = [rock, paper, scissors]
user_choice = int(input("enter 0 for rock, 1 for paper and 2 for sissaors : "))
if(user_choice > 2 or user_choice < 0):
  print("Invalid Input")
else:
  print(img[user_choice])
  
  computer_choice = random.randint(0,2)
  print(f"computer_choice :{computer_choice}"+img[computer_choice])

  if(computer_choice == user_choice):
    print("Draw")
  elif(user_choice == 0 and computer_choice == 2):
    print("You win!!!")
  elif(computer_choice == 0 and user_choice == 2):
    print("You lose")
  elif(user_choice > computer_choice ):
    print("You win!!!")
  elif(user_choice < computer_choice):
    print("You lose")
    
      