for _ in range(1, 11):
    t = int(input())
    target, sentence = input(), input()
    count = 0
    for i in range(len(sentence)-len(target)+1):
        for j in range(len(target)):
            if sentence[i+j] != target[j]:
                break
        else:
            count += 1
    print('#%s %s' % (t, count))
