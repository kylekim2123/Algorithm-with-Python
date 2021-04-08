# 5986. 새샘이와 세 소수

temp = []
primes = [0, 0] + list(range(2, 1000))
for i in range(2, 1000):
    if primes[i]:
        for j in range(i+i, 1000, i):
            primes[j] = 0
        temp.append(primes[i])


len_temp = len(temp)
for t in range(1, int(input())+1):
    n = int(input())
    count = 0
    for i in range(len_temp):
        if temp[i] >= n:
            break
        if temp[i]:
            for j in range(i, len_temp):
                if temp[j] >= n:
                    break
                if temp[j]:
                    for k in range(j, len_temp):
                        if temp[k] >= n:
                            break
                        if temp[k] and temp[i]+temp[j]+temp[k] == n:
                            count += 1
    print(f'#{t} {count}')