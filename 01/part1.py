import sys
from typing import List


def get_larger_count(measurements: List[int]) -> int:
    count: int = 0
    for i in range(len(measurements) - 1):
        if measurements[i+1] > measurements[i]:
            count += 1
    return count


if __name__ == '__main__':
    # lines = sys.stdin.readlines()
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    measurements = list(map(int, [line.strip() for line in lines]))
    count = get_larger_count(measurements)
    print(count)
