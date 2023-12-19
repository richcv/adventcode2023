import os
import sys
from pathlib import Path
INPUT_FILE = "input_small2.txt"

def count_paths(matrix, x, y, path, paths, visited):
    # Base case: if we reach the end point, add the path to the collection of paths
    if x == len(matrix[0])-1 and y == len(matrix)-1:
        print(f"Hit the end!  Adding this one. (Up to {len(paths)})")
        paths.append(path)
        return

    # Recursive case: add the current position to the path and continue exploring
    if x+1 < len(matrix[0]) and (x+1, y) not in visited:
        visited.add((x+1, y))
        count_paths(matrix, x+1, y, path+matrix[y][x+1], paths, visited)
        visited.remove((x+1, y))
    if x-1 > 0 and (x-1, y) not in visited:
        visited.add((x-1, y))
        count_paths(matrix, x-1, y, path+matrix[y][x-1], paths, visited)
        visited.remove((x-1, y))
    if y+1 < len(matrix) and (x, y+1) not in visited:
        visited.add((x, y+1))
        count_paths(matrix, x, y+1, path+matrix[y+1][x], paths, visited)
        visited.remove((x, y+1))
    if y-1 > 0 and (x, y-1) not in visited:
        visited.add((x, y-1))
        count_paths(matrix, x, y-1, path+matrix[y-1][x], paths, visited)
        visited.remove((x, y-1))

# Example usage
#matrix = [
#    ['A', 'B', 'C', 'D', 'E', 'F'],
#    ['G', 'H', 'I', 'J', 'K', 'L'],
#    ['M', 'N', 'O', 'P', 'Q', 'R'],
#    ['S', 'T', 'U', 'V', 'W', 'X']
#]

# ---------------------------------------------------
# Main
# ---------------------------------------------------   
script_path = os.path.realpath(__file__)

script_dir = os.path.dirname(script_path)
FILE = os.path.join(script_dir, INPUT_FILE)

data = Path(FILE).read_text()
matrix = [[int(c) for c in line.strip()] for line in data.splitlines()]


start_x, start_y = 0, 0
end_x, end_y = len(matrix[0]) - 1, len(matrix) - 1
paths = []
visited = {(0, 0)}
count_paths(matrix, start_x, start_y, matrix[start_y][start_x], paths, visited)
num_paths = len(paths)
print(f"There are {num_paths} unique character strings from ({start_x}, {start_y}) to ({end_x}, {end_y}) in the given matrix.")
print("Here are the unique character strings:")
for path in paths:
    print(path)
