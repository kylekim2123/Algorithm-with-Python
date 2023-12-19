for t in range(1, int(input())+1):
    n, hex_num = input().split()
    result = format(int(hex_num, 16), 'b').zfill(int(n)*4)
    print('#%s %s' % (t, result))