import sys
from typing import List, Tuple

OXYGEN_RATING = '1'
CO2_RATING = '0'


def remove_insignificant(*, sig_bit: str, report_data: List[str]) -> List[str]:
    tempList = report_data[:]
    for idx in range(len(report_data) - 1, -1, -1):
        if not tempList[idx].startswith(sig_bit):
            tempList.pop(idx)

    return tempList


def get_max_bit(row: List[str]) -> str:
    return '1' if row.count('1') >= (len(row) / 2) else '0'


def get_min_bit(row: List[str]) -> str:
    return '0' if row.count('0') <= (len(row) / 2) else '1'


def get_rating(data: List[str], rating: str) -> str:

    if len(data[0]) == 0:
        return ''

    if len(data) == 1:
        return data[0]
    else:
        bitsToConsider = [row[0] for row in data]

        significantBit = get_max_bit(
            bitsToConsider) if rating == OXYGEN_RATING else get_min_bit(bitsToConsider)

        updatedList = remove_insignificant(
            sig_bit=significantBit,
            report_data=data
        )

        return significantBit + get_rating([row[1:] for row in updatedList], rating)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    report = [line.strip()for line in lines]

    oxygen = get_rating(report, OXYGEN_RATING)
    co2 = get_rating(report, CO2_RATING)

    print(int(oxygen, 2) * int(co2, 2))
