"""
Conway's Game of Life, by Graeme Benson

Original code can be found at
https://nostarch.com/big-book-small-python-projects

More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""
import copy
import random
import sys
import time

# Set up grid constants
width = 80
height = 20

# Set up characters representing cell types
live_cell = '0'
dead_cell = ' '

# next_cells is a dictionary based on the values of alive and dead cells
next_cells = {}

# Initialize grid with random cells
for x in range(width):
    for y in range(height):
        if random.randint(0, 1) == 1:
            next_cells[(x, y)] = live_cell
        else:
            next_cells[(x, y)] = dead_cell

# Main program loop
while True:

    cells = copy.deepcopy(next_cells)

    # Print cells on screen
    print("_" * width)
    for y in range(height):
        for x in range(width):
            print(cells[(x, y)], end = "")
        print()
    print("_" * width)
    print("Press Ctrl+C to quit.")

    # Calculate the next step's cells based on the current step's cells
    for x in range(width):
        for y in range(height):
            # Get neighboring cells
            left = (x-1) % width
            right = (x+1) % width
            above = (y-1) % height
            below = (y+1) % height

            # Count number of living neighbors
            n_neighbors = 0
            if cells[(left, above)] == live_cell:
                n_neighbors += 1
            if cells[(right, above)] == live_cell:
                n_neighbors += 1
            if cells[(left, below)] == live_cell:
                n_neighbors += 1
            if cells[(right, below)] == live_cell:
                n_neighbors += 1
            if cells[(x, above)] == live_cell:
                n_neighbors += 1
            if cells[(x, below)] == live_cell:
                n_neighbors += 1
            if cells[(left, y)] == live_cell:
                n_neighbors += 1
            if cells[(right, y)] == live_cell:
                n_neighbors += 1

            # Set cell based on Conway's Game of Life rules
            if cells[(x, y)] == live_cell and (n_neighbors == 2 or n_neighbors == 3):
                # Living cells with 2-3 neighbors stay alive
                next_cells[(x, y)] = live_cell
            elif cells[(x, y)] == dead_cell and n_neighbors == 3:
                # Dead cells with 3 neighbors become alive
                next_cells[(x, y)] = live_cell
            else:
                # Everything else dies or stays dead
                next_cells[(x, y)] = dead_cell
    try:
        time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nConway's Game of Life\n" \
              + "by Graeme Benson")
        sys.exit()
