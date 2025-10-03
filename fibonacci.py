#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    try:
        n = int(input("How many terms? "))
        if n > 0: break
    except: pass
    print("Please enter a positive integer.")

a, b = 0, 1
for i in range(n):
    print(a, end=" " if i < n - 1 else "\n")
    a, b = b, a + b
