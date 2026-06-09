#                       ROCK PAPER SCISSORS
# You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

import random

rock=''' 
     ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

      '''
paper=''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

      '''
scissor='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

list=[rock, paper, scissor]

user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))

if user_choice>=0 and user_choice<=2:
    print(list[user_choice])
    

computer_choice= random.randint(0,2)
print("computer_choice:")
print(list[computer_choice])


if user_choice>=3 or user_choice<0:
    print("You type an invalid number. You lose :/")
elif user_choice == computer_choice:
    print("It's a draw ;)")
elif user_choice>computer_choice:
    print("You win:)")
elif computer_choice>user_choice:
    print("You lose:/")
elif computer_choice==0 and user_choice==2:
    print("You lose:/")
elif user_choice==0 and computer_choice==2:
    print("You Win:)")