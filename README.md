# Guess-The-Number-Game

This Python script implements a simple "Guess the Number" game where the player has to guess a randomly generated number between 0 and 5. The player starts with a certain amount of virtual currency and can win or lose currency based on their guesses.

## Features
- Provides a user-friendly interface for playing the game.
- Allows the player to choose if they are a beginner or specify their starting currency.
- Generates a random number for the player to guess.
- Awards currency for correct guesses and penalizes for incorrect ones.
- Ends the game if the player's currency reaches zero or exceeds a certain threshold.

## Usage
1. Run the Python script.
2. Follow the on-screen instructions to specify if you are a beginner or input your starting currency.
3. Guess a number between 0 and 5 when prompted.
4. Receive feedback on your guess and see your current currency balance.
5. Continue playing until you run out of currency or reach a specific winning threshold.

## Rules
- The player's currency is initially set to $10 if they are a beginner. Otherwise, they can specify their starting amount.
- Each correct guess awards the player $1.
- Each incorrect guess deducts $1 from the player's balance.
- If the player's balance reaches zero, the game ends.
- If the player's balance exceeds $20, they win $100 and the game ends.

## Dependencies
This script only uses Python's built-in `random` module for generating random numbers.

## Contributing
Contributions to improve the game, such as adding new features or refining the user interface, are welcome. Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
