import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_numbers = []  # List to store guessed numbers
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                break
            
            guessed_numbers.append(guess)  # Add the guessed number to the list
        except ValueError:
            print("Please enter a valid integer.")

    # Create a dictionary to store game statistics
    game_stats = {
        "secret_number": secret_number,
        "attempts": attempts,
        "guessed_numbers": guessed_numbers
    }
    
    return game_stats

if __name__ == "__main__":
    result = number_guessing_game()
    print("\nGame Statistics:")
    print(f"Secret Number: {result['secret_number']}")
    print(f"Total Attempts: {result['attempts']}")
    print(f"Guessed Numbers: {result['guessed_numbers']}")



