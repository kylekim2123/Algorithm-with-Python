# 1208. S/W 문제해결 기본 1일차 - Flatten

for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort(reverse=True)
    
    for _ in range(dump):
        max_number_idx = boxes.index(max(boxes))
        min_number_idx = boxes.index(min(boxes))
        boxes[max_number_idx] -= 1
        boxes[min_number_idx] += 1

        if max(boxes) == min(boxes):
            break

    print(f'#{t} {max(boxes) - min(boxes)}')
