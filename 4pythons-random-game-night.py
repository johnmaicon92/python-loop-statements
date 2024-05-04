"""
Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. 
Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.
"""

import random
items = ["Boomerang", "Ball", "Pen", "Shoes"]
item = random.choice(items)

for item in items:
    guess = input(f"Guess which item was selected (Boomerang, Ball, Pen, Shoes): ")
    if guess == item:
        print(f"You guessed correctly!")
    else:
        print(f"You guessed incorrectly!")