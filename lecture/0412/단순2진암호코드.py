NUMBERS = {
    '0001101': 0, 
    '0011001': 1, 
    '0010011': 2, 
    '0111101': 3, 
    '0100011': 4, 
    '0110001': 5, 
    '0101111': 6, 
    '0111011': 7, 
    '0110111': 8, 
    '0001011': 9
}

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    for line in arr:
        passcode = line.rstrip('0')
        if passcode:
            end = len(passcode)
            start = end - 56
            break
    code = [NUMBERS[passcode[i:i+7]] for i in range(start, end, 7)]
    check = ((code[0]+code[2]+code[4]+code[6]) * 3) + (code[1]+code[3]+code[5]) + code[7]
    result = 0 if check % 10 else sum(code)
    print('#%s %s' % (t, result))