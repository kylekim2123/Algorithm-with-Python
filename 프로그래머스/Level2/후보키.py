# 2019 KAKAO BLIND RECRUITMENT 후보키 (Level 2)

from itertools import combinations


def solution(relation):
    def is_visited(index):
        for v in visited:
            if not (v - index):
                return True
        return False

    cols = [[i] + list(line) for i, line in enumerate(zip(*relation))]
    visited = []
    answer = 0

    for i in range(1, len(cols) + 1):
        for case in combinations(cols, i):
            index, *row = list(zip(*case))
            index = set(index)

            if is_visited(index):
                continue

            if len(set(row)) == len(row):
                answer += 1
                visited.append(index)

    return answer
