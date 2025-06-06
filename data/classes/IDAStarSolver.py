from typing import List, Optional, Tuple
import heapq
class IDAStarSolver:
    def __init__(self, initial_values: List[Optional[int]]):
        self.initial_values = tuple(0 if x is None else x for x in initial_values)
        self.goal_values = tuple(range(1, 16)) + (0,)
        self.manhattan_lookup = self.precompute_manhattan_distances()


    def precompute_manhattan_distances(self) -> dict[int, Tuple[int, int]]:
        """Precompute Manhattan distances for each tile to its goal position."""
        lookup = {}
        for tile in range(1, 16):
            goal_row, goal_col = (tile - 1) // 4, (tile - 1) % 4
            lookup[tile] = (goal_row, goal_col)
        return lookup
    
    
    def manhattan_distance(self, state: Tuple[int, ...]) -> int:
        """Uses a precomputed lookup table for faster Manhattan distance calculation."""
        distance = 0
        for i, tile in enumerate(state):
            if tile != 0:
                goal_row, goal_col = self.manhattan_lookup[tile]
                current_row, current_col = i // 4, i % 4
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance
    def walking_distance(self, state: Tuple[int, ...]) -> int:
        """Correct implementation of the Walking Distance heuristic."""
        vertical_counts = [0] * 4
        horizontal_counts = [0] * 4

        for idx in range(16):
            tile = state[idx]
            if tile == 0:
                continue

            # Vertical: Check if tile is in its target row
            target_row = (tile - 1) // 4
            current_row = idx // 4
            if current_row == target_row:
                vertical_counts[target_row] += 1

            # Horizontal: Check if tile is in its target column
            target_col = (tile - 1) % 4
            current_col = idx % 4
            if current_col == target_col:
                horizontal_counts[target_col] += 1

        target_vertical = [4, 4, 4, 3]  # Target tiles per row
        target_horizontal = [4, 4, 4, 3]  # Target tiles per column

        # Calculate absolute differences for rows and columns
        vertical_diff = sum(abs(vertical_counts[i] - target_vertical[i]) for i in range(4))
        horizontal_diff = sum(abs(horizontal_counts[i] - target_horizontal[i]) for i in range(4))

        # Each move fixes one row and one column difference
        return (vertical_diff + horizontal_diff) // 2
    def misplaced_tiles(self, state: Tuple[int, ...]) -> int:
        """Counts the number of tiles that are not in their goal positions."""
        return sum(1 for i, tile in enumerate(state) if tile != 0 and tile != self.goal_values[i])
    
    def linear_conflict(self, state: Tuple[int, ...]) -> int:
        conflict = 0
        for row in range(4):
            max_val = -1
            for col in range(4):
                index = row * 4 + col
                value = state[index]
                if value != 0 and (value - 1) // 4 == row:
                    if value > max_val:
                        max_val = value
                    else:
                        conflict += 2

        for col in range(4):
            max_val = -1
            for row in range(4):
                index = row * 4 + col
                value = state[index]
                if value != 0 and (value - 1) % 4 == col:
                    if value > max_val:
                        max_val = value
                    else:
                        conflict += 2

        return conflict

    def corner_conflict(self, state: Tuple[int, ...]) -> int:
        conflict = 0
        corners = [(0, 1, 4), (3, 2, 7), (12, 8, 13), (15, 11, 14)]
        for corner, side1, side2 in corners:
            if state[corner] != 0 and state[corner] != self.goal_values[corner]:
                if state[side1] != 0 and state[side1] == self.goal_values[corner]:
                    conflict += 2
                if state[side2] != 0 and state[side2] == self.goal_values[corner]:
                    conflict += 2
        return conflict

    def heuristic(self, state: Tuple[int, ...]) -> int:
        return (
            self.manhattan_distance(state) +
            self.linear_conflict(state) +
            self.corner_conflict(state) 
            # self.walking_distance(state)
        )

    def get_neighbors(self, empty_index: int) -> List[int]:
        neighbors = []
        row, col = empty_index // 4, empty_index % 4
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 4 and 0 <= new_col < 4:
                neighbors.append(new_row * 4 + new_col)
        return neighbors

    def search(self, state: Tuple[int, ...], g: int, bound: int, path: List[Tuple[int, ...]]) -> Tuple[int, Optional[List[Tuple[int, ...]]]]:
        f = g + self.heuristic(state)
        if f > bound:
            return f, None
        if state == self.goal_values:
            return f, path 
        min_bound = float('inf')
        empty_index = state.index(0)
        for new_index in self.get_neighbors(empty_index):
            new_state = list(state)
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            new_tuple = tuple(new_state)
            if new_tuple not in path:
                path.append(new_tuple)
                t, result = self.search(new_tuple, g + 1, bound, path)
                if result is not None:
                    return t, result
                if t < min_bound:
                    min_bound = t
                path.pop()
        return min_bound, None

    def solve(self) -> Optional[List[Tuple[int, ...]]]:
        bound = self.heuristic(self.initial_values)
        path = []
        while True:
            t, result = self.search(self.initial_values, 0, bound, path)
            if result is not None:
                return result
            if t == float('inf'):
                return None
            bound = t


