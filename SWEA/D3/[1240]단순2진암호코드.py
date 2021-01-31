# 1240. S/W 문제해결 응용 1일차 - 단순 2진 암호코드

for t in range(1, int(input())+1):
    nm = list(map(int, input().split()))
    arrays = [list(input()) for _ in range(nm[0])]

    for line in arrays:
        if '1' in line:
            passcode = line # 1이 있다는건, 암호가 있다는것이므로 passcode에 그 줄을 저장하고 break
            break
    for i in range(nm[1]-1, -1, -1):
        if passcode[i] == '1':
            end_point = i + 1
            break
    start_point = end_point - 56

    passcode = passcode[start_point:end_point]
    numbers = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    code = []
    
    for i in range(0, len(passcode)-6, 7):
        unit = passcode[i:i+7]
        code.append(numbers.index(''.join(unit)))
    
    verification = ((code[0]+code[2]+code[4]+code[6]) * 3) + (code[1]+code[3]+code[5]) + code[7]
    if verification % 10 == 0:
        print(f'#{t} {sum(code)}')
    else:
        print(f'#{t} 0')
