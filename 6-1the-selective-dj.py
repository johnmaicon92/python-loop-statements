"""
Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres. 
Use slicing to create a sublist of genres from the second to the fourth track.
"""


genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = ["Just feel it!", "You ROCK!!!", "Let's Dance!", "Peaceful and Quiet!"]
genre_messages = dict(zip(genres, messages))
sublist = genres[1:5]
for i, genre in enumerate(sublist):
    print(f"{i + 1}. {genre}")
    print(genre_messages[genre])
