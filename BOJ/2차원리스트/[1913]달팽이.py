# 1913. 달팽이 (실버4)

n = int(input())  # 표의 크기
find_number = int(input())  # 찾는 숫자
board = [[0] * n for _ in range(n)]  # 표 (0으로 초기화)

x, y, direction = 0, 0, 0  # 시작 위치, 방향 초기화
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하, 우, 상, 좌

# n 제곱부터 거꾸로 작성
for i in range(n * n, 0, -1):
    # 찾는 숫자가 나오면 좌표 기록
    if i == find_number:
        find_x, find_y = x + 1, y + 1

    board[x][y] = i  # 표에 숫자 기록
    dx, dy = dxy[direction]  # 방향에 따른 변량 설정
    nx, ny = x + dx, y + dy  # 이동

    # 표를 벗어나지 않고, 빈 공간인 경우 -> 이동
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        x, y = nx, ny
    # 표를 벗어나거나, 이미 다른 숫자가 있는 경우 -> 방향 전환 & 이동
    else:
        direction = (direction + 1) % 4
        dx, dy = dxy[direction]
        x, y = x + dx, y + dy

# 전체 표 출력
for line in board:
    for number in line:
        print(number, end=" ")
    print()

# 찾는 숫자의 좌표 출력
print(find_x, find_y)
