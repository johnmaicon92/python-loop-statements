"""
Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. 
For each genre, print out the track number and a message that the light show is ready. 
Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.
"""

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    if genres[i] == 'Classical':
              continue
    print(f"{i+1} {genres[i]}")
    print("The light show is ready!")
