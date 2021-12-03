"""
Collatz Sequence (3n+1 Problem), by Graeme Benson

Original code can be found at
https://nostarch.com/big-book-small-python-projects
"""
import sys
import time

print("""\nThe Collatz Sequence, or 3n+1 problem, is a sequence of numbers
starting from n, following three rules:
1. If n is even, the next number n is n/2
2. If n is odd, the next number n is 3n+1
3. If n is 1, the sequence terminates

It is generally thought, though as of yet mathematically unproven, that every
starting number n eventually ends at 1.

Let's try it. Enter a number greater than 0:\n""")

n = int(input("> "))

print()
while n != 1:
    if n % 2 == 0:
        n = n //2
    else:
        n = 3*n+1

    print(str(n) + ", ", end = "", flush = True)
    time.sleep(0.05)
print()
