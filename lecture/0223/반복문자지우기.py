def erase(word, start):
    for i in range(start, len(word)-1):
        if word[i] == word[i+1]:
            start = i-1 if i > 0 else 0
            return erase(word.replace(word[i]+word[i+1], ''), start)
    return len(word)


for t in range(1, int(input())+1):
    word = input()
    print('#%s %s' % (t, erase(word, 0)))
