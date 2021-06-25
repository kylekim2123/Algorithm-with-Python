from itertools import combinations
from typing import List


def solution(N: int) -> List:
    odds: List[int] = [number for number in range(1, N+1) if number % 2]
    for i in range(len(odds), 0, -1):
        for case in combinations(odds, i):
            if sum(case) == N:
                return list(case)
    return []
