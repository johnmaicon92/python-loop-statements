"""
Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. 
Extend this task by adding a counter that displays the number of the track before the genre.

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
"""

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = ["Just feel it!", "You ROCK!!!", "Let's Dance!", "Peaceful and Quiet!"]
genre_messages = dict(zip(genres, messages))

for i, genre in enumerate(genres):
    print(f"{i + 1}. {genre}")
    print(genre_messages[genre])
