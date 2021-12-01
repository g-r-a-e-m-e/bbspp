"""
Birthday Problem Simulation

Inspired by Al Sweigart's "Birthday Paradox Simulation.""
Additional info at https://en.wikipedia.org/wiki/Birthday_problem
Original code can be found at https://nostarch.com/big-book-small-python-projects
"""

import math

def get_p_bar(num_birthdays):
    n = num_birthdays
    p_bar = (math.factorial(365))/((365**n)*math.factorial(365 - n))
    return p_bar

num_birthdays = int(input("Enter a number between 1 and 100. "))
p = 100 * (1 - round(get_p_bar(num_birthdays), 4))
print("The probability of two birthdays falling on the same day is approximately {}%.".format(p))
