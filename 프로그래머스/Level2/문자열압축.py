# 2020 KAKAO BLIND RECRUITMENT 문자열 압축 (Level 2)


def solution(s):
    min_length = len(s)

    for i in range(1, len(s) // 2 + 1):
        length, counts = 0, 0
        prev = s[:i]

        for j in range(0, len(s), i):
            now = s[j : j + i]
            if prev == now:
                counts += 1
            else:
                length += len(prev)
                if counts > 1:
                    length += len(str(counts))
                prev = now
                counts = 1

        length += len(prev)
        if counts > 1:
            length += len(str(counts))
        min_length = min(min_length, length)

    return min_length
