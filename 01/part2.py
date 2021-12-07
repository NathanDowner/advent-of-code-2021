import sys
from typing import List


def get_larger_count_with_sliding_window(measurements: List[int], window_size: int = 1) -> int:
    count: int = 0
    for i in range(len(measurements) - window_size):
        if sum(measurements[i+1:i+1 + window_size]) > sum(measurements[i: i+window_size]):
            count += 1
    return count


if __name__ == '__main__':
    # lines = sys.stdin.readlines()
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    measurements = list(map(int, [line.strip() for line in lines]))
    count = get_larger_count_with_sliding_window(measurements, window_size=3)
    print(count)
