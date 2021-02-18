for t in range(1, int(input())+1):
    str1, str2 = input(), input()
    counts = [str2.count(char) for char in str1]
    print('#%s %s' % (t, max(counts)))
