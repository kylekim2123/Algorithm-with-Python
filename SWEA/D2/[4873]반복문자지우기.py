# 4873. 반복 문자 지우기

# 풀이1. 반복 문자 지우고 바로 전 인덱스부터 탐색 시작
for t in range(1, int(input())+1):
    word = input()
    i = 0
    while i < len(word):
        for j in range(len(word)-1):
            if word[j] == word[j+1]:
                serial = word[j] + word[j+1]
                serial_i = j
                break
        else:
            serial_i = -1
        if serial_i != -1:
            word = word.replace(serial, '')
            i = serial_i - 1 if i > 0 else 0
            continue
        i += 1
    result = len(word) if word else 0
    print('#%s %s' % (t, result))

# 풀이2. 반복 문자 지우고 처음부터 탐색 시작
for t in range(1, int(input())+1):
    word = input()
    i = 0
    while i < len(word):
        serial = word[i] + word[i]
        if serial in word:
            word = word.replace(serial, '')
            i = 0
            continue
        i += 1
    result = len(word) if word else 0
    print('#%s %s' % (t, result))

        