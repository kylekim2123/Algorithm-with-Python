# 2022 KAKAO BLIND RECRUITMENT 양궁대회 (Level 2)

from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_diff = 0

    for case in combinations_with_replacement(range(11), n):
        # 1. 라이언의 기록
        ryan = [0] * 11

        for i in case:
            ryan[10 - i] += 1

        # 2. 어피치와 라이언 점수 합 비교
        apeach_total = 0
        ryan_total = 0

        for i in range(11):
            if info[i] == 0 and ryan[i] == 0:  # 둘 다 못맞췄으면 합산 안함
                continue
            if info[i] >= ryan[i]:
                apeach_total += 10 - i
            else:
                ryan_total += 10 - i

        # 3. 최종 답 도출
        diff = ryan_total - apeach_total

        if diff <= 0 or diff < max_diff:  # 라이언이 졌거나, 이겼어도 가장 큰 점수차가 아니면
            continue

        if diff == max_diff:
            # 동일 점수 차 나왔을 때, 낮은 점수 과녁을 더 많이 맞춘 기록으로 변경
            for i in range(11):
                if ryan[10 - i] < answer[10 - i]:
                    break
            else:
                answer = ryan
        else:
            # 동일 점수 차가 아니면 그냥 갱신
            max_diff = diff
            answer = ryan

    return answer
