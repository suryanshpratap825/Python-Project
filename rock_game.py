import random
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

game=[rock,paper,scissors]
user=int(input("What do you choose? Tyepe 0 for Rock. 1 for Paper or 2 for Scissors.\n"))
computer_choice=random.randint(0,2)
# print(f"Computer Choose {computer_choice}")
if(user>3 or user<0):
  print("You type a invalid number so you lose!")
else:
  print(game[user])
  print(f"Computer Choose{computer_choice}")
  print(game[computer_choice])
  if user==0 and computer_choice==2:
    print("you win")
  elif computer_choice==0 and user==2:
    print("You Lose!")
  elif computer_choice>user:
    print("You lose!")
  elif user<computer_choice:
    print("You win!")
  elif user==computer_choice:
    print("Its Dwar!")
# if user==0 and computer_choice==2:
#   print("You Wins!")
# elif computer_choice==0 and user==2:
#   print("You lose!")
# elif(computer_choice>user):
#   print("You lose!")
# elif user==computer_choice:
#   print("Its Draw!")
# elif computer_choice>user and user>:
#   print("You Win!")
# else:
#   print("You type a invalid number so you lose!")
