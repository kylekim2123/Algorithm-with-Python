# 10570. 제곱 팰린드롬 수

def is_palindrome(number):
    s, e = 0, len(number)-1
    while s < e:
        if number[s] != number[e]:
            return False
        s += 1
        e -= 1
    return True

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    total = 0
    for i in range(a, b+1):
        sqrt_number = i**(0.5)
        int_sqrt_number = int(sqrt_number)
        if sqrt_number != int_sqrt_number:
            continue
        if is_palindrome(str(i)) and is_palindrome(str(int_sqrt_number)):
            total += 1
    print(f'#{t} {total}')
