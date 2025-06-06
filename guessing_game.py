import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed_correctly:
        try:
            # Get user input for their guess
            user_guess_str = input("Enter your guess: ")
            user_guess = int(user_guess_str) # Convert input to an integer
            attempts += 1 # Increment the attempt count

            # Provide feedback based on the guess
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                guessed_correctly = True # Set to True to exit the loop
        except ValueError:
            # Handle cases where the user inputs non-numeric data
            print("Invalid input. Please enter a whole number.")
            # attempts are not incremented for invalid input as it's not a valid guess
        except KeyboardInterrupt:
            # Handle Ctrl+C to exit gracefully
            print("\nExiting the game. Goodbye!")
            break # Exit the loop if user presses Ctrl+C

# Call the function to start the game
if __name__ == "__main__":
    play_guessing_game()