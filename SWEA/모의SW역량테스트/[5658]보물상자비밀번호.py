# 5658. 보물상자 비밀번호

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    hex_num = list(input())
    jump = n // 4
    cases = set()
    while True:
        temp = len(cases)
        cases.update([''.join(hex_num[i:i+jump]) for i in range(0, n-2, jump)])
        if temp == len(cases):
            break
        hex_num.append(hex_num.pop(0))
    result = sorted(list(map(lambda x: int(x, 16), cases)), reverse=True)
    print(f'#{t} {result[k-1]}')