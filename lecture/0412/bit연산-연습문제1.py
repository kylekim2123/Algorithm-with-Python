def binary_to_int(binary_number):
    unit = 2**(len(binary_number)-1)
    int_num = 0
    for binary_digit in binary_number:
        int_num += binary_digit * unit
        unit //= 2
    return int_num

BIT = 7
for t in range(1, int(input())+1):
    binary_line = list(map(int, input()))
    result = [binary_to_int(binary_line[i:i+BIT]) for i in range(0, len(binary_line), BIT)]
    print('#%s' % t, ', '.join(map(str, result)))