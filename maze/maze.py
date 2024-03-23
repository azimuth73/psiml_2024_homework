from typing import Tuple
from PIL import Image
import numpy as np


class Maze:
    def __init__(self, maze_image: np.array, teleport_positions: np.array) -> None:
        self.num_rows, self.num_cols, _ = maze_image.shape
        self.teleport_positions = teleport_positions
        # Extract the RGB channels (because most images in the public set are in RGBA format)
        rgb_channels = maze_image[..., :3]
        # Check if each pixel is white (255, 255, 255) and create a boolean array for traversable pixels of the maze
        self.traversable = np.all(rgb_channels == [255, 255, 255], axis=-1)

    def __str__(self):
        maze_str = ''
        for row in self.traversable:
            for pixel in row:
                maze_str += '.' if pixel else '#'
            maze_str += '\n'  # Newline at the end of each row
        maze_str += 'Teleport Positions:\n'
        for position in self.teleport_positions:
            row, col = position
            maze_str += f'\trow={row}\n'
            maze_str += f'\tcol={col}\n\n'
        return maze_str

    def calculate_num_entrances(self) -> int:
        num_entrances = 0
    
        # TODO: Calculate num_entrances
    
        return num_entrances
    
    def calculate_shortest_path_length(self) -> int:
        shortest_path_length = -1
    
        # TODO: Calculate shortest_path_len
    
        return shortest_path_length
    
    def calculate_shortest_path_length_teleports(self) -> int:
        shortest_path_length_teleports = -1
    
        # TODO: Calculate shortest_path_len_teleports
    
        return shortest_path_length_teleports


def solve_maze(maze_image_path: str, teleport_positions: np.array) -> Tuple[int, int, int]:
    maze_image_file = Image.open(maze_image_path)
    maze_image = np.array(maze_image_file)

    maze = Maze(maze_image, teleport_positions)

    num_entrances = maze.calculate_num_entrances()
    shortest_path_length = maze.calculate_shortest_path_length()
    shortest_path_length_teleports = maze.calculate_shortest_path_length_teleports()

    return num_entrances, shortest_path_length, shortest_path_length_teleports


def main() -> None:
    maze_image_path = input()
    num_teleports = int(input())

    teleport_positions = np.empty(shape=(num_teleports, 2), dtype=int)
    for i in range(num_teleports):
        row, col = input().split()
        teleport_positions[i] = (row, col)

    num_entrances, shortest_path_length, shortest_path_length_teleports = solve_maze(maze_image_path, teleport_positions)
    print(num_entrances)
    print(shortest_path_length)
    print(shortest_path_length_teleports)


if __name__ == '__main__':
    main()
