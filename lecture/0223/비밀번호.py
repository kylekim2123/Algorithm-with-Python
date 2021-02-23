for t in range(1, 11):
    n, word = input().split()
    stack = []
    for unit in word:
        if stack and stack[-1] == unit:
            stack.pop()
            continue
        stack.append(unit)
    print('#%s %s' % (t, ''.join(stack)))
