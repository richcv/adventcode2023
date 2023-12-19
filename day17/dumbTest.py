import os
import sys
import heapq
from pathlib import Path
from typing import Self

#FILE = "test.txt" if len(sys.argv) <= 1 else sys.argv[1]
INPUT_FILE = "input_small.txt"


MAX_STEPS = 3

MAX_STEPS_TWO = 10
MIN_STEPS_TWO = 4


# ---------------------------------------------------
# Node
# ---------------------------------------------------   
class Node:
    def __init__(
        self,
        heat_cost: int,
        position: tuple[int, int],
        streak: int,
        direction: str,
    ):
        self.heat_cost = heat_cost
        self.position = position
        self.streak = streak
        self.direction = direction

    def to_hashable(self) -> tuple[tuple[int, int], int, str]:
        return (self.position, self.streak, self.direction)

    # For heapq
    def __lt__(self, other):
        return self.heat_cost < other.heat_cost

    # For visited
    def __hash__(self):
        return hash(self.to_hashable())

    def __eq__(self, other):
        return self.to_hashable() == other.to_hashable()

    def __repr__(self):
        return f"Node(heat_cost={self.heat_cost}, position={self.position}, streak={self.streak}, direction={self.direction})"


    def get_neighbors(self, width: int, height: int) -> list[Self]:
        opposite_direction = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        neighbors = []
        for direction in ['up', 'down', 'left', 'right']:
            if direction == opposite_direction[self.direction]:
                continue
            if direction == self.direction and self.streak >= MAX_STEPS:
                continue

            new_position = self.increment_by_directions(direction)

            if not is_possible_position(new_position, width, height):
                continue

            new_streak = self.streak + 1 if direction == self.direction else 1

            # Heat cost is not imortant here
            neighbors.append(Node(0, new_position, new_streak , direction))

        return neighbors

    def get_neighbors_two(self, width: int, height: int) -> list[Self]:
        opposite_direction = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        neighbors = []
        for direction in ['up', 'down', 'left', 'right']:
            if (
                direction == opposite_direction[self.direction] or
                (direction == self.direction and self.streak >= MAX_STEPS_TWO) or
                (direction != self.direction and self.streak < MIN_STEPS_TWO)
            ):
                continue


            new_position = self.increment_by_directions(direction)

            if not is_possible_position(new_position, width, height):
                continue

            new_streak = self.streak + 1 if direction == self.direction else 1

            # Heat cost is not imortant here
            neighbors.append(Node(0, new_position, new_streak, direction))

        return neighbors


    def increment_by_directions(self, direction: str):
        match direction:
            case 'up':
                return (self.position[0], self.position[1] - 1)
            case 'down':
                return (self.position[0], self.position[1] + 1)
            case 'left':
                return (self.position[0] - 1, self.position[1])
            case 'right':
                return (self.position[0] + 1, self.position[1])
            case _:
                raise ValueError(f'Unknown direction: {direction}')


# ---------------------------------------------------
# Grid 
# ---------------------------------------------------   
class Grid:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

        self.queue = [
            Node(heat_cost=0, position=(0, 0), streak=0, direction='right'),
            Node(heat_cost=0, position=(0, 0), streak=0, direction='down'),
        ]

    def find_path(self) -> int:
        """
        This can work cause we first check least heat costed path, so it will work
        totally like diskstra algorithm. So when we reach the finish we are done.
        When we update neighbor we do it from least path first, so we don't need to
        check saved heat cost of neighbor.

        Kudos to heapq.
        """
        visited = set()
        while self.queue:
            node = heapq.heappop(self.queue)

            if node.position == (self.width - 1, self.height - 1):
                return node.heat_cost

            if node in visited:
                continue

            visited.add(node)

            for neighbor in node.get_neighbors(self.width, self.height):
                new_heat_cost = node.heat_cost + self.get_heat_cost(neighbor.position)
                neighbor.heat_cost = new_heat_cost

                heapq.heappush(self.queue, neighbor)

        raise ValueError("No path found")


    def get_heat_cost(self, position: tuple[int, int]) -> int:
        return self.grid[position[1]][position[0]]

    def find_path_two(self) -> int:
        visited = set()
        while self.queue:
            node = heapq.heappop(self.queue)

            if node.position == (self.width - 1, self.height - 1):
                if node.streak < MIN_STEPS_TWO:
                    continue

                return node.heat_cost

            if node in visited:
                continue
            visited.add(node)

            for neighbor in node.get_neighbors_two(self.width, self.height):
                new_heat_cost = node.heat_cost + self.get_heat_cost(neighbor.position)
                neighbor.heat_cost = new_heat_cost
                heapq.heappush(self.queue, neighbor)

        raise ValueError("No path found")


def is_possible_position(position: tuple[int, int], width: int, height: int) -> bool:
   x, y = position
   return 0 <= x < width and 0 <= y < height


# ---------------------------------------------------
# Main
# ---------------------------------------------------   
script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
FILE = os.path.join(script_dir, INPUT_FILE)

data = Path(FILE).read_text()
grid_data = [[int(c) for c in line.strip()] for line in data.splitlines()]

for theRow in grid_data:
   print (f"{theRow}")

grid = Grid(grid_data)
result = grid.find_path()
print(f"The number is... {result}")

#grid = Grid(grid_data)
#result = grid.find_path_two()
#print("Part two: ", result)