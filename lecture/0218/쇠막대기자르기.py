for t in range(1, int(input())+1):
    line = input()
    pieces = []
    count = 0
    for bracket in line:
        if bracket == '(':
            pieces.append(0)
            continue
        if pieces[-1] == 0:
            pieces.pop()
            for i in range(len(pieces)):
                pieces[i] += 1
            continue
        count += pieces.pop()+1
    print('#%s %s' % (t, count))