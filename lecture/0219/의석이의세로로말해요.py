for t in range(1, int(input())+1):
    result = [''] * 15
    for _ in range(5):
        word = input()
        for i in range(len(word)):
            result[i] += word[i]
    print('#%s %s' % (t, ''.join(result)))
