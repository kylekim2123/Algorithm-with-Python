result = []
for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    mask = (1 << n) - 1
    check = 'ON' if m & mask == mask else 'OFF'
    result.append('#%s %s' % (t, check))
print('\n'.join(result))
