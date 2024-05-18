# 2018 KAKAO BLIND RECRUITMENT 비밀지도 (Level 1)


def solution(n, arr1, arr2):
    board = []

    for i in range(n):
        b1 = format(arr1[i], "b").zfill(n)
        b2 = format(arr2[i], "b").zfill(n)

        line = ""
        for j in range(n):
            if b1[j] == "1" or b2[j] == "1":
                line += "#"
            else:
                line += " "

        board.append(line)

    return board
