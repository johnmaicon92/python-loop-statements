"""
Task 1: Loop Condition Exploration
Write a while loop with a condition that will never be false (an infinite loop). Inside the loop, print a statement. Then, use a break statement to exit the loop after 5 iterations.
"""
cookies = 1
while cookies > 0:
    print(str(cookies+1))
    cookies += 1
    if cookies == 12:
        break
