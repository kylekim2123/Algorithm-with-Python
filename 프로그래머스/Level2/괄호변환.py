# 2020 KAKAO BLIND RECRUITMENT 괄호 변환 (Level 2)


def solution(p):
    # 1
    if not p:
        return p

    # 2
    u = ""
    total = 0
    is_correct = True

    for i, bracket in enumerate(p):
        u += bracket
        total += 1 if bracket == "(" else -1
        if total < 0:  # ')'가 한번이라도 '('보다 많다면 올바르지 못한 상태
            is_correct = False
        if total == 0:
            break

    v = p[i + 1 :]

    # 3
    if is_correct:
        return u + solution(v)
    # 4
    else:
        temp = "(" + solution(v) + ")"
        for bracket in u[1:-1]:
            temp += ")" if bracket == "(" else "("
        return temp


print(solution("(()())()"))
