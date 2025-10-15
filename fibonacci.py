#!/usr/bin/env python3

# Fibonacci Sequence – Lab 3
# Prompts for a positive integer and prints that many Fibonacci terms.

def get_positive_int(prompt="How many terms? "):
    while True:
        s = input(prompt)
        try:
            n = int(s)
            if n > 0:
                return n
        except ValueError:
            pass
        print("Please enter a positive integer.")

n = get_positive_int()

a, b = 0, 1
terms = []
for _ in range(n):
    terms.append(str(a))
    a, b = b, a + b

print(" ".join(terms))
