for t in range(1, int(input())+1):
    n = float(input())
    binary = []
    while n:
        n *= 2.0
        bi_digit = int(n)
        binary.append(bi_digit)
        n -= bi_digit
    result = ''.join(map(str, binary)) if len(binary) <= 12 else 'overflow'
    print('#%s %s' % (t, result))
