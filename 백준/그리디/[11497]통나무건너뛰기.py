# 11497. 통나무 건너뛰기 (실버1)

for t in range(int(input())):
    n = int(input())
    woods = list(map(int, input().split()))
    woods.sort()
    
    left, right = [], []
    for i in range(n):
        if i % 2:
            right.append(woods[i])
        else:
            left.append(woods[i])
    
    result = left + sorted(right, reverse=True)
    max_level = abs(result[0]-result[-1])
    for i in range(n-1):
        level = abs(result[i] - result[i+1])
        max_level = max(level, max_level)

    print(max_level)
