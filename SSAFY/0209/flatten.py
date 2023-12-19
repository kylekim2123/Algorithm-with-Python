def get_index_of_max_min(args):
    max_num, min_num = args[0], args[0]
    max_index, min_index = 0, 0
    for i in range(len(args)):
        if args[i] > max_num:
            max_num = args[i]
            max_index = i
        elif args[i] < min_num:
            min_num = args[i]
            min_index = i
    return max_index, min_index


for t in range(1, 11):
    dumps = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(dumps):
        max_idx, min_idx = get_index_of_max_min(boxes)
        if boxes[max_idx] <= boxes[min_idx]+1:
            result = boxes[max_idx] - boxes[min_idx]
            break
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    else:
        max_idx, min_idx = get_index_of_max_min(boxes)
        result = boxes[max_idx] - boxes[min_idx]
    print('#%s %s' % (t, result))