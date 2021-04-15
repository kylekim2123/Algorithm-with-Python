for t in range(1, int(input())+1):
    numbers, n = input().split()
    length = len(numbers)
    cases = {numbers}
    for _ in range(int(n)):
        changed = set()
        for case in cases:
            case_list = list(case)
            for i in range(length):
                for j in range(i+1, length):
                    case_list[i], case_list[j] = case_list[j], case_list[i]
                    changed.add(''.join(case_list))
                    case_list[i], case_list[j] = case_list[j], case_list[i]
        cases = changed
    print('#%s %s' % (t, max(map(int, cases))))
        