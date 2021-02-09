T = int(input())
for t in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))

    length = len(boxes)
    drops = [0] * length
    for i in range(length):
        count = 0
        for j in range(length):
            if boxes[i] <= boxes[j]:
                count += 1
        drops[i] = length - i - count

    max_drop = 0
    for drop in drops:
        if drop > max_drop:
            max_drop = drop

    print('#%s %s' % (t, max_drop))
