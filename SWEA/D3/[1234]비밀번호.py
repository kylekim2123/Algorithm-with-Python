# 1234. S/W 문제해결 기본 10일차 - 비밀번호

for t in range(1, 11):
    inputs = list(input().split())
    length = int(inputs[0])
    password = list(inputs[1])

    while(True):
        index = 0
        while index < length - 1:
            if password[index] == password[index+1]:
                password.pop(index)
                password.pop(index) # 위에서 pop을 했는데, 밑에서 index를 그대로 쓰는 이유는, pop을 했기 때문에 index -= 1이 알아서 적용됨
                length -= 2
                break
            index += 1
        else:
            break
    print(f'#{t} {"".join(password)}')