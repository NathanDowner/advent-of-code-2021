import sys
from typing import List, Tuple


def get_gamma_epsilon(report: List[List[str]]) -> Tuple[str, str]:
    gamma = ''
    epsilon = ''
    transposed_report = list(zip(*report))
    for row in transposed_report:
        if row.count('1') > (len(row) / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return gamma, epsilon


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    report = [list(line.strip())for line in lines]

    gamma_rate_bin, epsilon_rate_bin = get_gamma_epsilon(report)

    print(int(gamma_rate_bin, 2) * int(epsilon_rate_bin, 2))
