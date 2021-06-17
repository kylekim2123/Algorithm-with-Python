from typing import List

def solution(A: List) -> int:
    P: str = '0'
    MAX_CARS: int = 10**9
    stringified_A: str = ''.join(str(car) for car in A)
    Q_groups: List = stringified_A.split(P)[1:] # 0번째 값은 쓸모 없으므로 제외
    Q_lengths: List = [len(Q_group) for Q_group in Q_groups]

    total_Q_lengths: int = sum(Q_lengths)
    passing_cars: int = total_Q_lengths

    for Q_length in Q_lengths:
        total_Q_lengths -= Q_length
        passing_cars += total_Q_lengths

    return passing_cars if passing_cars <= MAX_CARS else -1