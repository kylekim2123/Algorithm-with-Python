# 1289. 원재의 메모리 복구하기

for t in range(1, int(input())+1):
    origin = str(int(input()))
    if origin == '0':
        print('#%s 0' % t)
        continue
    count = 1
    for i in range(1, len(origin)):
        count += 1 if origin[i-1] != origin[i] else 0
    print('#%s %s' % (t, count))