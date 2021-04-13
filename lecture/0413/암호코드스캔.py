import sys
sys.stdin = open("lecture/0413/input.txt", "r")

NUMBERS = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9
}

def hex_to_bin(hex_num):
    if hex_num == '0':
        return '0000'
    return format(int(hex_num, 16), 'b').zfill(4)


def change_to_bin_code(hex_code):
    if not hex_code:
        return ''
    binary_code = []
    for hex_digit in hex_code:
        binary_code.append(hex_to_bin(hex_digit))
    return ''.join(binary_code).rstrip('0')


def validate_and_calculate(code):
    check = ((code[0]+code[2]+code[4]+code[6]) * 3) + (code[1]+code[3]+code[5]) + code[7]
    return 0 if check % 10 else sum(code)


def find_ratios(binary_code, i):
    second, third, fourth = 0, 0, 0
    while binary_code[i] == '1':
        fourth += 1
        i -= 1
    while binary_code[i] == '0':
        third += 1
        i -= 1
    while binary_code[i] == '1':
        second += 1
        i -= 1
    while i >= 0 and binary_code[i] == '0':
        i -= 1
    min_ratio = min(second, third, fourth)
    return i, [second//min_ratio, third//min_ratio, fourth//min_ratio]


def sum_code_number(code_arr):
    total = 0
    checked = set()
    for binary_code in code_arr:
        if binary_code:
            i = len(binary_code) - 1
            code = []
            while i >= 0:
                i, ratios = find_ratios(binary_code, i)
                code_key = ''.join(map(str, ratios))
                code.append(NUMBERS[code_key])
                if len(code) == 8:
                    checked_code = ''.join(map(str, code))
                    if checked_code not in checked:
                        checked.add(checked_code)
                        total += validate_and_calculate(code[::-1])
                    code = []
    return total


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    code_arr = [change_to_bin_code(input()[:m].rstrip('0')) for _ in range(n)]
    print('#%s %s' % (t, sum_code_number(code_arr)))
