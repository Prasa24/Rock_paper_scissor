import random
print("🚨Want to play enter ""Yes""🚨")
#user input
entry=input()
# loop for playing continuously
while entry.lower()!='no':
    print("Welcome to Rock, Paper, Scissors Game 🎉👋🏻")

    # Get player choice
    player = input("Enter your choice: ").lower()

    # Get computer choice
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        print("You win! 🎉")
    elif player in choices:
        print("You lose! 😢")
    else:
        print("Invalid choice❌")
    print("Thanks for playing🙌")
    print("🚨Want to continue type ""Yes""🚨 \n 🚨want to stop type ""No""🚨")
    entry=input().lower()
else:
    print("You have chosen not play 😔")   
