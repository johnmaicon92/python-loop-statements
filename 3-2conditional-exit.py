"""
Task 2: Conditional Exit
Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. 
The loop should terminate naturally once the condition is met.
"""

cookies = 1
while cookies < 12:
    print(str(cookies))
    cookies += 1
print(f"{cookies} cookies to share with friends")