def hex_to_binary_four_digits(hex_number):
    hex_to_int_num = int(hex_number, 16)
    int_to_binary_num = format(hex_to_int_num, 'b')
    return int_to_binary_num.zfill(4)

for t in range(1, int(input())+1):
    hex_line = input()
    binary_line = ''
    for hex_num in hex_line:
        binary_line += hex_to_binary_four_digits(hex_num)
    
    result = []
    for i in range(0, len(binary_line), 7):
        binary_to_int_num = int(binary_line[i:i+7], 2)
        result.append(binary_to_int_num)
    print('#%s' % t, ', '.join(map(str, result)))