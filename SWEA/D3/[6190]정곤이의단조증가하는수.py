# 6190. 정곤이의 단조 증가하는 수

def is_increment(number):
    number_list = []
    while number > 0:
        number_list.append(number % 10)
        number //= 10
    for i in range(len(number_list)-1):
        if number_list[i] < number_list[i+1]:
            return False
    return True

for t in range(1, int(input())+1):
    n = int(input())
    A = list(map(int, input().split()))
    result = -1
    for i in range(n-1):
        for j in range(i+1, n):
            number = A[i] * A[j]
            if number < 10 or not number % 10:
                continue
            if is_increment(number):
                result = max(result, number)
    print(f'#{t} {result}')
