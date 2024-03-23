from typing import Tuple
from PIL import Image
import numpy as np


def solve_maze(maze_image_path) -> Tuple[int, int, int]:
    maze_image_file = Image.open(maze_image_path)
    maze_image = np.array(maze_image_file)

    num_entrances = 0
    shortest_path_len = -1
    shortest_path_len_teleports = -1

    # TODO: logic to solve maze and calculate return values

    return num_entrances, shortest_path_len, shortest_path_len_teleports


def main() -> None:
    maze_image_path = input()
    num_entrances, shortest_path_len, shortest_path_len_teleports = solve_maze(maze_image_path)
    print(num_entrances)
    print(shortest_path_len)
    print(shortest_path_len_teleports)


if __name__ == '__main__':
    main()
