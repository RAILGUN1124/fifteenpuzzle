# /* PuzzleInstance.py

import pygame

from data.classes.FifteenPuzzle import FifteenPuzzle
from data.classes.HumanPlayer import HumanPlayer
from data.classes.AStarSolver import AStarSolver
from data.classes.IDAStarSolver import IDAStarSolver
import time
def puzzle_instance(player: HumanPlayer, initial_values: list[int | None]):
    
    
    if isinstance(player, HumanPlayer):
        pygame.init()
        WINDOW_SIZE = (600, 600)
        screen = pygame.display.set_mode(WINDOW_SIZE)
        board = FifteenPuzzle(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
        if not board.set_squares(initial_values):
            print("Invalid initial values!")
            return
        # Human player logic
        moves_count = 0
        running = True
        while running:
            chosen_action = player.choose_action(board)
            moves_count += 1
            if chosen_action == False or moves_count > 1000:
                print('Player did not solve')
                running = False
            elif board.is_solved():
                print('Player solved!')
                board.highlight()
                running = False
            board.draw()

        viewing = True
        while viewing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    viewing = False
    elif isinstance(player, AStarSolver):
        # A* solver logic
        start_time = time.time()
        solution_path = player.solve()
        end_time = time.time()

        if solution_path:
            print(f"Solution found in {len(solution_path)} moves!")
            print(f"Running time: {end_time - start_time:.2f} seconds")
            for step, state in enumerate(solution_path,start=1):
                state_with_none = [None if x == 0 else x for x in state]
                print(f"Step {step}: {state_with_none}")
            return len(solution_path) - 1, end_time - start_time
        else:
            print("Time limit exceeded. No solution found!")
    elif isinstance(player, IDAStarSolver):
        # A* solver logic
        start_time = time.time()
        solution_path = player.solve()
        end_time = time.time()

        if solution_path:
            print(f"Solution found in {len(solution_path)} moves!")
            print(f"Running time: {end_time - start_time:.2f} seconds")
            for step, state in enumerate(solution_path,start=1):
                state_with_none = [None if x == 0 else x for x in state]
                print(f"Step {step}: {state_with_none}")
            return len(solution_path) - 1, end_time - start_time
        else:
            print("Time limit exceeded. No solution found!")


# /* PuzzleInstance.py

# import pygame

# from data.classes.FifteenPuzzle import FifteenPuzzle
# from data.classes.HumanPlayer import HumanPlayer
# from data.classes.AStarSolver import AStarSolver
# import time
# def puzzle_instance(player: HumanPlayer, initial_values: list[int | None]):
#     pygame.init()
#     WINDOW_SIZE = (600, 600)
#     screen = pygame.display.set_mode(WINDOW_SIZE)
#     board = FifteenPuzzle(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
#     if not board.set_squares(initial_values):
#         print("Invalid initial values!")
#         return
    
#     if isinstance(player, HumanPlayer):
    
#         # Human player logic
#         moves_count = 0
#         running = True
#         while running:
#             chosen_action = player.choose_action(board)
#             moves_count += 1
#             if chosen_action == False or moves_count > 1000:
#                 print('Player did not solve')
#                 running = False
#             elif board.is_solved():
#                 print('Player solved!')
#                 board.highlight()
#                 running = False
#             board.draw()

#         viewing = True
#         while viewing:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     viewing = False
#     elif isinstance(player, AStarSolver):
#         # A* solver logic
#         start_time = time.time()
#         solution_path = player.solve()
#         end_time = time.time()

#         if solution_path:
#             print(f"Solution found in {len(solution_path) - 1} moves!")
#             print(f"Running time: {end_time - start_time:.2f} seconds")

#             # Display each step on the board
#             for step, state in enumerate(solution_path):
#                 # Convert 0 back to None for rendering
#                 state_with_none = [None if x == 0 else x for x in state]
#                 board.set_squares(state_with_none)
#                 board.draw()

#                 # Add a delay for visualization
#                 pygame.time.wait(2500)  # 500ms delay between steps

#                 # Handle Pygame events to prevent freezing
#                 for event in pygame.event.get():
#                     if event.type == pygame.QUIT:
#                         pygame.quit()
#                         return
#         else:
#             print("No solution found!")

#     # Allow the player to view the result
#     viewing = True
#     while viewing:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 viewing = False