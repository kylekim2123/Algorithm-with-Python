# 2021 KAKAO BLIND RECRUITMENT 메뉴 리뉴얼 (Level 2)

from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for i in course:
        cases = []
        for order in orders:
            cases.extend(combinations(sorted(order), i))

        menus = Counter(cases).most_common()
        answer.extend(
            "".join(menu) for menu, cnt in menus if cnt == menus[0][1] and cnt >= 2
        )

    return sorted(answer)
