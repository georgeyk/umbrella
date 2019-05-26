# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import random
import time
import sys


def create_grid(n):
    grid = []
    for i in range(n):
        grid.append([bool(random.randint(0, 1)) for col in range(n)])

    return grid


def display(grid, generation):
    # clear screen
    print(chr(27) + "[2J")

    state = ""
    for row in grid:
        for value in row:
            state += "⬛️" if value else "⬜️"

        state += "\n"

    state += "\nGeneration: {}".format(generation)
    print(state)


def count_alive_neighbours(grid, row, column):
    order = len(grid)
    count = 0
    for x in (row - 1, row, row + 1):
        for y in (column - 1, column, column + 1):
            if x == row and y == column:
                continue

            if x >= 0 and x < order and y >= 0 and y < order:
                count += 1 if grid[x][y] else 0

    return count


def calculate_next_generation(grid):
    next_gen_states = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            alive = count_alive_neighbours(grid, i, j)
            if value:
                if alive < 2 or alive > 3:
                    next_gen_states.append((i, j, False))
            else:
                if alive == 3:
                    next_gen_states.append((i, j, True))

    return next_gen_states


def create_generations(grid_size, generations, interval=0.2):
    grid = create_grid(grid_size)
    for i in range(generations):
        next_generation_states = calculate_next_generation(grid)

        if not next_generation_states:
            break

        for row, col, value in next_generation_states:
            grid[row][col] = value

        display(grid, i)
        time.sleep(interval)


if __name__ == "__main__":
    try:
        create_generations(grid_size=20, generations=1000)
    except KeyboardInterrupt:
        print("\nbye!")
        sys.exit(1)
    else:
        sys.exit(0)
