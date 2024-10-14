# Snake-Water-Gun-by-Python
## Description

This Python script implements the classic game of Snake, Water, Gun. Players choose one of these three options, and the computer randomly selects one as well. The winner is determined based on the following rules:

• Gun beats Snake

• Water beats Gun

• Snake beats Water

If both players choose the same option, it's a draw.

## How to Play

1. Clone the Repository:
   
Bash

  git clone https://github.com/HappySR/Snake-Water-Gun-by-Python.git

Use code with caution.

2. Run the Script:
   
Bash

  python swg.py

Use code with caution.

3. Follow the Prompts: Enter your choice (s, w, or g) when prompted.
   
## Code Structure

The code is organized into the following sections:

• **Variable Definitions**: Defines the symbols for Snake, Water, and Gun.

• **Dictionary Creation**: Creates dictionaries to map symbols to their corresponding values and vice versa.

• **Computer Choice**: Randomly generates the computer's choice.

• **User Input**: Prompts the user to enter their choice.

• **Result Calculation**: Determines the winner based on the chosen options.

• **Output**: Displays the choices of both players and the result of the game.

## Example Usage

Enter your choice: s

You chose Snake

Computer chose Water

You Win!

## Customization

You can customize the game by:

• **Adding more options**: Expand the dictionary to include additional choices.

• **Changing the rules**: Modify the conditions for determining the winner.

• **Implementing a scoring system**: Track the number of wins, losses, and draws.
