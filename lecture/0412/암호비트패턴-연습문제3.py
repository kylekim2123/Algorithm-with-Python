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
    hex_to_int_num = int(hex_number, 16) # 16진수 -> 10진수
    int_to_binary_num = format(hex_to_int_num, 'b') # 10진수 -> 2진수
    return int_to_binary_num.zfill(4) # 4자리로 맞춰줌(공백은 0으로 채운다)

def find_patterns(binary_number):
    i, result = 0, []
    while i < len(binary_line):
        pattern = binary_line[i:i+6] # 패턴은 6자리
        if len(pattern) < 6:
            break # 6자리 패턴이 아니라면(즉, 마지막에 남은 잔여 패턴이라면) 암호탐색을 끝낸다.
        if pattern in PATTERNS: # 암호비트패턴에 등록된 패턴이라면
            result.append(PATTERNS[pattern]) # 패턴 -> 숫자
            i += 6 # 6칸 뛰어 넘는다
            continue
        i += 1 # 등록되지 않은 패턴이라면, 1칸만 이동 후 다시 탐색
    return result

for t in range(1, int(input())+1):
    hex_line = input()
    binary_line = ''
    for hex_num in hex_line:
        binary_line += hex_to_binary_four_digits(hex_num) # 16진수 -> 2진수
    print('#%s' % t, ', '.join(map(str, find_patterns(binary_line)))) # 패턴 해독 후, 출력
    