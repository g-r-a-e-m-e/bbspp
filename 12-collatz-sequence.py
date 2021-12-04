"""
Collatz Sequence (3n+1 Problem), by Graeme Benson

Original code can be found at
https://nostarch.com/big-book-small-python-projects
"""
import time
import random
import datetime as dt

print("""\nThe Collatz Sequence, or 3n+1 problem, is a sequence of numbers
starting from n, following three rules:
    1. If n is even, the next number n is n/2
    2. If n is odd, the next number n is 3n+1
    3. If n is 1, the sequence terminates

It is generally thought, though as of yet mathematically unproven, that every
starting number n eventually ends at 1.

Let's try it.\n""")

seconds_to_run = int(input("Enter the number of seconds the program should run: "))

print("\nRunning...")

end = dt.datetime.now() + dt.timedelta(seconds = seconds_to_run)
results = {}
while dt.datetime.now() <= end:
    n_list = []
    n = random.randint(1, 10**10)
    n_list.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n //2
            n_list.append(n)
        else:
            n = 3*n+1
            n_list.append(n)
        result = {n_list[0]: len(n_list)}
        results.update(result)

max_int = max(results, key = lambda x: results[x])
max_len = results[max_int]
num_ints = len(results)

print("\nThe integer with the longest sequence is " \
        +  str(max_int) \
        + " with a total of " \
        + str(max_len) \
        + " steps to 1. " \
        + str(num_ints) \
        + " integers were tested in " \
        + str(seconds_to_run) \
        + " seconds.\n")
