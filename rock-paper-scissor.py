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

#Write your code below this line 👇
import random
print("Welcome to the rock, paper, scissors game!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices = [rock, paper, scissors]
if user_choice > 2 or user_choice < 0:
  print("You chose a wrong number, you lose!")
else:
  print(choices[user_choice])


  comp_choice = random.randint(0,2)
  print(f"Computer chose: {comp_choice}")
  print(choices[comp_choice])
  
  if comp_choice == 0 and user_choice == 1:
    print("You win!")
  elif comp_choice == 1 and user_choice == 2:
    print("You win!")
  elif comp_choice == 2 and user_choice == 0:
    print("You win!")
  elif comp_choice == user_choice:
    print("It's a tie")
  else:
    print("You lose")
  
