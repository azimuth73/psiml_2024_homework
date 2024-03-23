from typing import Tuple
from PIL import Image
import numpy as np


def calculate_num_entrances(maze_image: np.array) -> int:
    num_entrances = 0

    # TODO: Calculate num_entrances

    return num_entrances


def calculate_shortest_path_len(maze_image: np.array) -> int:
    shortest_path_len = -1

    # TODO: Calculate shortest_path_len

    return shortest_path_len


def calculate_shortest_path_len_teleports(maze_image: np.array, teleport_positions: np.array) -> int:
    shortest_path_len_teleports = -1

    # TODO: Calculate shortest_path_len_teleports

    return shortest_path_len_teleports


def solve_maze(maze_image_path: str, teleport_positions: np.array) -> Tuple[int, int, int]:
    maze_image_file = Image.open(maze_image_path)
    maze_image = np.array(maze_image_file)

    num_entrances = calculate_num_entrances(maze_image)
    shortest_path_len = calculate_shortest_path_len(maze_image)
    shortest_path_len_teleports = calculate_shortest_path_len_teleports(maze_image, teleport_positions)

    return num_entrances, shortest_path_len, shortest_path_len_teleports


def main() -> None:
    maze_image_path = input()
    num_teleports = int(input())

    teleport_positions = np.empty(num_teleports)

    for i in range(num_teleports):
        row, col = input().split()

        teleport_positions[i] = (row, col)

    num_entrances, shortest_path_len, shortest_path_len_teleports = solve_maze(maze_image_path, teleport_positions)
    print(num_entrances)
    print(shortest_path_len)
    print(shortest_path_len_teleports)


if __name__ == '__main__':
    main()
