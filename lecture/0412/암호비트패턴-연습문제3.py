PATTERNS = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

def hex_to_binary_four_digits(hex_number):
    hex_to_int_num = int(hex_number, 16)
    int_to_binary_num = format(hex_to_int_num, 'b')
    return int_to_binary_num.zfill(4)

def find_patterns(binary_number):
    i, result = 0, []
    while i < len(binary_line):
        pattern = binary_line[i:i+6]
        if len(pattern) < 6:
            break
        if pattern in PATTERNS:
            result.append(PATTERNS[pattern])
            i += 6
            continue
        i += 1
    return result

for t in range(1, int(input())+1):
    hex_line = input()
    binary_line = ''
    for hex_num in hex_line:
        binary_line += hex_to_binary_four_digits(hex_num)
    print('#%s' % t, ', '.join(map(str, find_patterns(binary_line))))
    