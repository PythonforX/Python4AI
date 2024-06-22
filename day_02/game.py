import random

options = ['rock', 'paper', 'scissors']

user_input = input("Enter the choice : ")
computer_choice = random.choice(options)
print(f"Computer'choice : {computer_choice}")

if user_input == computer_choice:
    print("it's a tie")

elif (user_input == 'rock' and computer_choice == 'scissors') or (user_input == 'scissors' and computer_choice == 'paper') or (user_input == 'paper' and computer_choice == 'rock'):
    print("User wins")

else:
    print("Computer wins")
