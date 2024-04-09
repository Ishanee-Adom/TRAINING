#This is a number guessing game
import random

print("Welcome To Number Guessing Game:")
print("I have selected a number between 1 to 100 can you guess it?")
secret_number=random.randint(1,100)
attempt=0



while True:
    guess=int(input("Enter any random number of your choice  "))
    attempt = attempt + 1

    if guess < secret_number:
        print("Number is too low; Try again")
    elif guess > secret_number:
        print("Number is too high; Try again")
    else:     
        print(f"Congrats! You've guess the correct number, which is {secret_number}")
        print(f"It took you {attempt} attempt")
        break
    