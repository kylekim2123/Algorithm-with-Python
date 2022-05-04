# 2019 KAKAO BLIND RECRUITMENT 실패율 (Level 1)

from collections import Counter


def solution(N, stages):
    no_clear = [0] * (N + 1)
    playing = Counter(stages)

    for i in range(1, N + 1):
        players = sum(playing[stage] for stage in playing if i <= stage)
        if players > 0:
            no_clear[i] = playing[i] / players

    return sorted((i for i in range(1, N + 1)), key=lambda x: no_clear[x], reverse=True)
