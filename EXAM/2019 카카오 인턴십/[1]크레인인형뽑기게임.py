# 2019 카카오 인턴십 1번 크레인 인형뽑기 게임

def solution(board, moves):
    stack = []
    answer = 0
    length = len(board)
    for move in moves:
        col = move - 1
        for row in range(length):
            if board[row][col]:
                if stack and stack[-1] == board[row][col]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[row][col])
                board[row][col] = 0
                break
    return answer
