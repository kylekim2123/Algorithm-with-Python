# 2018 KAKAO BLIND RECRUITMENT 다트 게임 (Level 1)


def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    answer = []
    i = 0

    while i < len(dartResult):
        dart = dartResult[i]

        if dart.isdecimal():
            if dartResult[i : i + 2] == "10":
                answer.append(10)
                i += 2
                continue
            answer.append(int(dart))
        elif dart in bonus:
            answer[-1] **= bonus[dart]
        elif dart == "*":
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif dart == "#":
            answer[-1] *= -1

        i += 1

    return sum(answer)
