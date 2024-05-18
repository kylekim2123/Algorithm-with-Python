# 2018 KAKAO BLIND RECRUITMENT 프렌즈4블록 (Level 2)


def solution(m, n, board):
    board = list(map(list, board))
    dx, dy = [0, 1, 1], [1, 0, 1]
    answer = 0

    while True:
        erase = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == "0":
                    continue

                temp = [(i, j)]

                for k in range(3):
                    ni, nj = i + dx[k], j + dy[k]
                    if board[i][j] != board[ni][nj]:
                        break
                    temp.append((ni, nj))
                else:
                    erase.update(temp)

        if not erase:
            return answer

        for i, j in erase:
            board[i][j] = "0"

        answer += len(erase)

        temp = []
        for col in zip(*board):
            line = "".join(col)
            line = line.replace("0", "")
            line = "0" * (m-len(line)) + line
            temp.append(list(line))
        
        board = list(map(list, zip(*temp)))


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
