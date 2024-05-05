#Game of rock, paper scissors
import random
def DisplayMenu():
    name= input("Enter Your Name:  ")
    print(f"WELCOME {name} TO ROCK PAPER SCISSORS GAME")

def getUserChoice():
    while True:
        user_choice=input("Enter Your Choice: Rock, Paper or Scissors ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice, Please enter rock, paper or scissors")

def getComputerChoice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determineWinner(user_choice, computer_choice):
    if user_choice==computer_choice:
        answer="It's a tie"
        return answer
    elif (user_choice=="rock" and computer_choice=="scissors") or \
        (user_choice=="paper" and computer_choice=="rock") or \
        (user_choice=="scissors" and computer_choice=="paper"):
        answer="You win"
        return answer

    else:
        answer="Computer win"
        return answer


def mainGame():
    DisplayMenu()
    while True:
        user_choice=getUserChoice()
        computer_choice=getComputerChoice()
        print(f"You chose {user_choice}")
        print(f"The computer chose {computer_choice}")
        print(determineWinner(user_choice, computer_choice))

        playAgain=input("Do you want to play the game again yes/no: ")
        if playAgain == "no":
            print("Thanks for playing")
            break

mainGame()









    