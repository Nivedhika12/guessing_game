# guessing_game
# MITS Internship - Number Guessing Game

This is a simple command-line interface (CLI) Number Guessing Game developed in Python as part of the MITS Internship program.

## Features

* **Random Number Generation:** The game generates a random secret number within a predefined range (1 to 100).
* **Interactive Gameplay:** Users can enter their guesses through the command line.
* **Hints:** The game provides feedback (too high, too low, or correct) to guide the user's guesses.
* **Attempt Counter:** Tracks and displays the number of attempts taken to guess the correct number.

## How to Play

1.  **Guess the Number:** The game will tell you that it's thinking of a number between 1 and 100.
2.  **Enter Your Guess:** Type a whole number and press Enter.
3.  **Receive Feedback:** The game will tell you if your guess was "Too low!", "Too high!", or if you guessed it correctly.
4.  **Keep Guessing:** Continue entering numbers until you find the secret number.
5.  **Congratulations!** Once you guess correctly, the game will reveal the number and how many attempts it took you.

## How to Run

To run this game on your local machine, follow these steps:

1.  **Prerequisites:**
    * **Python 3:** Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2.  **Clone the repository:**
    If you haven't already cloned your internship projects repository, do so using Git:
    ```bash
    git clone [https://github.com/your-username/Your-Internship-Repo-Name.git](https://github.com/your-username/Your-Internship-Repo-Name.git)
    ```
    (Replace `your-username` with your GitHub username and `Your-Internship-Repo-Name` with the actual name of your repository, e.g., `MITS-Internship-Projects`).

3.  **Navigate to the project directory:**
    Open your terminal or command prompt and change your current directory to where your `guessing_game.py` file is located within the cloned repository:
    ```bash
    cd Your-Internship-Repo-Name
    ```
    (Then, if `guessing_game.py` is in a subfolder, navigate further, e.g., `cd NumberGuessingGame`)

4.  **Run the application:**
    Execute the Python script using the Python interpreter:
    ```bash
    python guessing_game.py
    ```
    (On some systems, you might need to use `python3 guessing_game.py`)

## Code Structure

* The game logic is encapsulated within the `play_guessing_game()` function.
* It utilizes the `random` module for number generation.
* Includes basic error handling for non-integer inputs.

---
*Developed for MITS Internship*
