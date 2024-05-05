import random

def DisplayMenu():
    name = input("Enter Your Name: ")
    print(f"WELCOME {name} TO ROCK PAPER SCISSORS GAME")

def getUserChoice():
    while True:
        user_choice = input("Enter Your Choice: Rock, Paper, or Scissors ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def getComputerChoice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determineWinner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win"
    else:
        return "Computer wins"

def mainGame():
    DisplayMenu()
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while rounds_played < 5:
        user_choice = getUserChoice()
        computer_choice = getComputerChoice()
        print(f"You chose {user_choice}")
        print(f"The computer chose {computer_choice}")
        result = determineWinner(user_choice, computer_choice)
        print(result)

        if result == "You win":
            user_score += 1
        elif result == "Computer wins":
            computer_score += 1

        rounds_played += 1

    if user_score > computer_score:
        print(f"Congratulations! You've won")
    elif computer_choice > user_choice:
        print(f"You lost")
    
mainGame()