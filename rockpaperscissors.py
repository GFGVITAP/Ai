import random

def play_game():
    """Play a game of Rock,Paper,Scissors."""

    # Get the player's choice.
    player_choice = input("Rock/paper/scissors? ")

    # Generate the computer's choice.
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner.
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

# Play the game.
play_game()
