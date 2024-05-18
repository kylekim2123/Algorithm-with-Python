# 1966. 프린터 큐 (실버3)

for _ in range(int(input())):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))

    count = 0
    while True:
        if importance[0] == max(importance):
            importance.pop(0)
            count += 1
            if m == 0:
                break
        else:
            importance.append(importance.pop(0))
            if m == 0:
                m = len(importance)
        m -= 1
    print(count)