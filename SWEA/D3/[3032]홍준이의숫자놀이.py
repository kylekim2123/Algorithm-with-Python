# 3032. 홍준이의 숫자 놀이

# 확장된 유클리드 호제법(최대공약수를 1이라고 보았을 때)
def e_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        n, a, b = a//b, b, a%b
        x0, x1 = x1, x0-(n*x1)
        y0, y1 = y1, y0-(n*y1)
    return x0, y0

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    result = ' '.join(map(str, e_gcd(a, b)))
    print(f'#{t} {result}')