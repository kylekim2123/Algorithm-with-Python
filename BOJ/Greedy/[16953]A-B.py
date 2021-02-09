# 16953. A -> B (실버1)

a, b = input().split()
if b[-1] != '1' and int(b[-1]) % 2:
    print(-1)
else:
    count = 1
    while a != b:
        print(b, count)
        last = b[-1]
        print(last)
        if last == '1':
            b = b[:-1]
        elif int(last) % 2 == 0:
            b = str(int(b) // 2)
        else:
            print(-1)
            break
        if not b:
            print(-1)
            break
        count += 1
    else:
        print(count)