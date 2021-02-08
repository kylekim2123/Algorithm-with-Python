def get_maximum(*args):
    max_num = 0
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num


for t in range(1, 11):
    buildings = int(input())  # 빌딩의 개수
    heights = list(map(int, input().split()))  # 각 빌딩의 높이(처음 2개, 마지막 2개는 높이가 0)
    total = 0

    for i in range(2, len(heights) - 2):
        standard = get_maximum(heights[i-2], heights[i-1], heights[i+1], heights[i+2])
        center = heights[i]
        if standard >= center:
            continue
        total += center - standard

    print('#%s %s' % (t, total))