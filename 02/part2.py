import sys
from typing import List, Tuple


def get_final_position(directions: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    for direction, num in directions:
        if direction == 'forward':
            horizontal += num
            depth += aim * num
        elif direction == 'down':
            aim += num
        else:
            aim -= num

    return (horizontal, depth)


def transform(line: str) -> Tuple[str, int]:
    data = line.strip().split()
    return (data[0], int(data[1]))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    directions: List[Tuple[str, int]] = [transform(line) for line in lines]
    horizontal, depth = get_final_position(directions)
    print(horizontal * depth)
