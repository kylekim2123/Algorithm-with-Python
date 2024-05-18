# 2019 카카오 개발자 겨울 인턴십 크레인 인형 뽑기 (Level 1)


def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                if stack and stack[-1] == board[i][move]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move])
                board[i][move] = 0
                break

    return answer
