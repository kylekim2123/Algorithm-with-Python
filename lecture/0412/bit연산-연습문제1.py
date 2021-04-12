for t in range(1, int(input())+1):
    line = list(map(int, input()))
    result = []
    for i in range(0, len(line)-6, 7):
        int_num = 0
        number = 2**6
        for bi_digit in line[i:i+7]:
            int_num += bi_digit * number
            number //= 2
        result.append(int_num)
    print('#%s' % t, ', '.join(map(str, result)))