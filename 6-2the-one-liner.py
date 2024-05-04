"""
Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. 
Print this new list.
"""

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
new_list = [genre + " Music" for genre in genres]
print(new_list)