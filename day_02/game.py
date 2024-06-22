import random

print("Welcome to Rock-Paper-Scissors!")
print("Enter 'rock', 'paper', or 'scissors' to play.")

user_choice = input("Enter your choice: ").lower()

if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please restart the game and try again.")
else:
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
