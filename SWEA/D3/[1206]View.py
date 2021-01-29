# 1206. S/W 문제해결 기본 1일차 - View

for t in range(1, 11):
    buildings = int(input())  # 빌딩의 개수
    heights = list(map(int, input().split()))  # 각 빌딩의 높이(처음 2개, 마지막 2개는 높이가 0)
    total = 0

    for i in range(2, len(heights) - 2):
        standard = max(heights[i-2], heights[i-1], heights[i+1], heights[i+2])
        center = heights[i]
        if standard >= center:
            continue
        total += center - standard

    print(f'#{t} {total}')