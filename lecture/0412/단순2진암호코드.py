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
        passcode = line.rstrip('0') # 모두 0으로 이루어진 줄이라면 빈 리스트, 암호가 있는 줄이라면 비지 않은 리스트일 것이다.
        if passcode: # 따라서 암호가 있는 줄이라면,
            end = len(passcode) # 끝점 할당
            start = end - 56 # 암호의 길이는 56이므로, 시작점 = 끝 - 56
            break
    code = [NUMBERS[passcode[i:i+7]] for i in range(start, end, 7)] # 암호를 7칸씩 잘라서 해독한다.
    check = ((code[0]+code[2]+code[4]+code[6]) * 3) + (code[1]+code[3]+code[5]) + code[7] # 검증 식에 따라 값을 도출한다.
    result = 0 if check % 10 else sum(code) # 검증식에 따라 도출된 값을 검증한다. (올바르지 않으면 0, 올바르면 합을 구한다)
    print('#%s %s' % (t, result))