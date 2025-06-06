import argparse

from data.classes.PuzzleInstance import puzzle_instance
from data.classes.HumanPlayer import HumanPlayer
import random
from data.classes.AStarSolver import AStarSolver
from data.classes.IDAStarSolver import IDAStarSolver
solved_config = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def count_inversions(configuration):
    # Count the number of inversions (pairs of tiles out of order)
    one_d_configuration = [tile for tile in configuration if tile is not None]
    inversions = 0
    for i in range(len(one_d_configuration)):
        for j in range(i + 1, len(one_d_configuration)):
            if one_d_configuration[i] > one_d_configuration[j]:
                inversions += 1
    return inversions

def find_blank_position(configuration):
    # Find the row of the blank tile (None)
    index = configuration.index(None)
    row = index // 4  # 4 columns, so integer division gives the row index
    return row

def is_solvable(configuration):
    inversions = count_inversions(configuration)
    blank_row = find_blank_position(configuration)

    # The puzzle is solvable if the number of inversions is even and the row of the blank is odd, or vice versa
    if inversions % 2 == 0:
        return blank_row % 2 == 1
    else:
        return blank_row % 2 == 0
def generate_random_valid_configuration():
    """ Generate a random valid configuration by shuffling the tiles and placing None anywhere. """
    while True:
        random_config = solved_config[:]  # Copy the solved configuration
        random.shuffle(random_config)  # Shuffle the list
        blank_position = random.randint(0, 15)  # Randomly pick a position for None
        random_config.insert(blank_position, None)  # Insert None at the random position
        
        if len(random_config) > 16:
            random_config.pop()  # Ensure the list remains of size 16 (because `None` was added)

        if is_solvable(random_config):
            return random_config

def main():
    parser = argparse.ArgumentParser(description="Initialize player for the game.")
    parser.add_argument('--human', action='store_true', help="Used for human to play the puzzle")
    parser.add_argument('--a-star', action='store_true', help="Used for human to play the puzzle")
    parser.add_argument('--ida-star', action='store_true', help="Used for human to play the puzzle")
    args = parser.parse_args()
    if args.human:
        human_player = HumanPlayer()
        # Reversed Order
        # initial_values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None]
        # One move away from solved
        initial_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,None, 15]
        puzzle_instance(human_player, initial_values)
    if args.ida_star:
        random_configs = []
        # random_configs = [[1, 2, 3, 4, 5, 6, 7, 8, None, 10, 11, 12, 9, 13, 14, 15],
        #                   [1, 14, 3, 12, 8, 10, 11, 7, 9, None, 5, 4, 15, 6, 13, 2],
        #                   [7, 10, 3, 4, 14, None, 12, 8, 9, 2, 15, 6, 13, 5, 1, 11]
        #                   ]
        random_configs = [[15, 13, 6, 1, 11, 5, 4, 8, 2, 12, 9, None, 10, 14, 3, 7],
                          [10, 11, 15, 1, 4, 9, 8, 3, 6, 12, None, 14, 13, 5, 2, 7],
                          [8, 3, None, 9, 2, 13, 1, 6, 11, 10, 7, 4, 14, 12, 15, 5],
                          [4, 5, 15, 8, 9, 11, 12, 10, 1, 2, 14, 3, None, 7, 6, 13],
                          [3, 5, 9, 2, None, 14, 4, 10, 13, 11, 8, 7, 12, 6, 1, 15],
                          [9, 7, 4, 6, None, 5, 12, 15, 8, 10, 14, 3, 13, 1, 2, 11],
                          [5, 9, 1, 7, 15, 8, 2, 14, 13, 11, 12, 4, None, 6, 3, 10],
                          [8, 5, 3, 13, 1, 2, 14, 11, 7, None, 9, 6, 15, 4, 12, 10],
                          [15, 7, 1, 6, 8, 4, 9, 3, 5, 12, 10, 11, None, 13, 14, 2],
                          [12, 7, 14, None, 1, 9, 2, 5, 10, 13, 3, 6, 15, 11, 4, 8]]

                          
        total_configs = 10
        # while len(random_configs) < total_configs:
        #     config = generate_random_valid_configuration()
        #     if (config not in random_configs):  # Ensure uniqueness
        #         # print(f"Generated valid config: {config}\n")
        #         random_configs.append(config)
        total_len = 0
        total_time = 0
        for i, config in enumerate(random_configs):
            print(f"\nTesting configuration {i + 1}: {config}")
            a_star_solver = IDAStarSolver(config)
            moves, time_taken = puzzle_instance(a_star_solver, config)
            total_len += moves
            total_time += time_taken
        print(f"\nAverage {total_configs} runs")
        print(f"Average moves: {total_len / total_configs}")
        print(f"Average time: {(total_time / total_configs):2f} seconds")
    
    if args.a_star:
        # random_configs = [[15, 13, 6, 1, 11, 5, 4, 8, 2, 12, 9, None, 10, 14, 3, 7],
        #                   [10, 11, 15, 1, 4, 9, 8, 3, 6, 12, None, 14, 13, 5, 2, 7],
        #                   [8, 3, None, 9, 2, 13, 1, 6, 11, 10, 7, 4, 14, 12, 15, 5],
        #                   [4, 5, 15, 8, 9, 11, 12, 10, 1, 2, 14, 3, None, 7, 6, 13],
        #                   [3, 5, 9, 2, None, 14, 4, 10, 13, 11, 8, 7, 12, 6, 1, 15],
        #                   [9, 7, 4, 6, None, 5, 12, 15, 8, 10, 14, 3, 13, 1, 2, 11],
        #                   [5, 9, 1, 7, 15, 8, 2, 14, 13, 11, 12, 4, None, 6, 3, 10],
        #                   [8, 5, 3, 13, 1, 2, 14, 11, 7, None, 9, 6, 15, 4, 12, 10],
        #                   [15, 7, 1, 6, 8, 4, 9, 3, 5, 12, 10, 11, None, 13, 14, 2],
        #                   [12, 7, 14, None, 1, 9, 2, 5, 10, 13, 3, 6, 15, 11, 4, 8]]
        random_configs= []
        total_configs = 100
        while len(random_configs) < total_configs:
            config = generate_random_valid_configuration()
            if (config not in random_configs):  # Ensure uniqueness
                # print(f"Generated valid config: {config}\n")
                random_configs.append(config)
        total_len = 0
        total_time = 0
        for i, config in enumerate(random_configs):
            print(f"\nTesting configuration {i + 1}: {config}")
            a_star_solver = AStarSolver(config)
            moves, time_taken = puzzle_instance(a_star_solver, config)
            total_len += moves
            total_time += time_taken
        print(f"\nAverage {total_configs} runs")
        print(f"Average moves: {total_len / total_configs}")
        print(f"Average time: {(total_time / total_configs):2f} seconds")
            

if __name__ == '__main__':
    main()