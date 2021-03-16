# 17281. 야구 (골드4)

from itertools import permutations
import sys
input = sys.stdin.readline

players = [list(map(int, input().split())) for _ in range(int(input()))]
max_score = 0
for order in permutations([1, 2, 3, 5, 6, 7, 8, 9], 8):
    score = 0
    now_player = 0
    hit_order = sorted([(i, hit) for i, hit in enumerate((4,) + order)], key=lambda x: x[1])
    for player in players:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            now_score = player[hit_order[now_player][0]]
            if now_score == 0:
                out += 1
            elif now_score == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif now_score == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif now_score == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif now_score == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            now_player += 1
            if now_player > 8:
                now_player = 0
    max_score = max(max_score, score)
print(max_score)

