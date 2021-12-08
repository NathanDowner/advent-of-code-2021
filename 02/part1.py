import sys
from typing import List, Tuple


def get_final_position(directions: List[Tuple[str, int]]) -> Tuple[int, int]:
    x = 0
    y = 0
    for direction, num in directions:
        x += num if direction == 'forward' else 0
        y += num if direction == 'down' else 0
        y -= num if direction == 'up' else 0

    return (x, y)


def transform(line: str) -> Tuple[str, int]:
    data = line.strip().split()
    return (data[0], int(data[1]))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    directions: List[Tuple[str, int]] = [transform(line) for line in lines]
    horizontal, depth = get_final_position(directions)
    print(horizontal * depth)
