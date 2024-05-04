"""
Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. 
Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.
"""

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = ["Just feel it!", "You ROCK!!!", "Let's Dance!", "Peaceful and Quiet!"]
genre_messages = dict(zip(genres, messages))
index = 0
while index < len(genres):
    picked_genre = genres[index]
    print(f"{index+1} {picked_genre}")
    print(genre_messages[picked_genre])
    if picked_genre == 'Hip-hop':
        break
    index += 1