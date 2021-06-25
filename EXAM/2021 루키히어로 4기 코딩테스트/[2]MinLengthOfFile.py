from datetime import datetime
from typing import Dict, List


def calculate_size(size: str) -> int:
    UNIT_PREFIX: Dict[str, int] = {'K': 2**10, 'M': 2**20, 'G': 2**30}
    
    prefix: str = size[-1]
    if prefix not in UNIT_PREFIX:
        return int(size)
    number: int = int(size[:-1])
    return number * UNIT_PREFIX[prefix]


def is_satisfied(size: str, modified_date: str, name: str) -> bool:
    TILDE: str = '~'
    MAX_SIZE: int = 14 * (2**20)
    MIN_DATE: datetime = datetime.strptime('1990-01-31', '%Y-%m-%d')

    converted_size: int = calculate_size(size)
    converted_date: datetime = datetime.strptime(modified_date, '%Y-%m-%d')
    if (name[-1] == TILDE) and (converted_size < MAX_SIZE) and (converted_date > MIN_DATE):
        return True
    return False


def solution(S: str) -> str:
    lines: List[str] = S.split('\n')
    name_lengths: List[int] = []

    for line in lines:
        size, modified_date, name = line.split()
        if is_satisfied(size, modified_date, name):
            length: int = len(name.split('.')[0])
            name_lengths.append(length)

    return str(min(name_lengths)) if name_lengths else 'NO FILES'
