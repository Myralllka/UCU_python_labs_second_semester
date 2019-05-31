# Program for playing the game of Life.
from Gameoflife.lifegrid import LifeGrid
import time
import os

# Define the initial configuration of live cells.
INIT_CONFIG = [(1, 2), (2, 2), (3, 2)]


# Set the size of the grid.


def input_info(message):
    res = ''
    while not res:
        try:
            res = int(input(message))
        except ValueError:
            print('input must be integer')
    return res


print('please, input some information...')
GRID_WIDTH = input_info('grid width > ')
GRID_HEIGHT = input_info('grid height > ')
NUM_GENS = input_info('number of generations > ')


# Indicate the number of generations.

def main():
    # Constructs the game grid and configure it.
    grid = LifeGrid(GRID_HEIGHT, GRID_WIDTH)
    grid.configure(INIT_CONFIG)

    # Plays the game.
    os.system('clear')
    draw(grid)
    for i in range(NUM_GENS):
        time.sleep(.4)
        evolve(grid)
        os.system('clear')
        draw(grid)
    time.sleep(.1)


# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    live_cells = []

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (
                    neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells)


# Prints a text-based representation of the game grid.
def draw(grid):
    print(grid)


# Executes the main routine.
main()
