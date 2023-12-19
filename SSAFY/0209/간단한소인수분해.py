T = int(input())
for t in range(1, T+1):
    number = int(input())
    exponent = [0] * 5 # a, b, c, d, e
    factors = [2, 3, 5, 7, 11]
    for i in range(5):
        while number % factors[i] == 0:
            number //= factors[i]
            exponent[i] += 1
    print('#%s' % t, end=' ')
    print(*exponent)

