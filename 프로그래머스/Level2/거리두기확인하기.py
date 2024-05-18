# 2021 카카오 채용연계형 인턴십 거리두기 확인하기 (Level 2)


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def check(place):
    visited = [[False] * 5 for _ in range(5)]

    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] != "X":
                        if visited[nx][ny] or place[nx][ny] == "P":
                            return 0
                        visited[nx][ny] = True

    return 1


def solution(places):
    return [check(place) for place in places]
