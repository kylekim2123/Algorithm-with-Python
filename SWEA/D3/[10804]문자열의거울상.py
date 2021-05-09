# 10804. 문자열의 거울상

MIRROR = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

for t in range(1, int(input())+1):
    print(f'#{t} {"".join([MIRROR[digit] for digit in input()[::-1]])}')