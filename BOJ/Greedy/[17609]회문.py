# 17609. 회문 (실버1)
def another_loop(word, i, j):
    while i <= len(word)//2:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

for _ in range(int(input())):
    word = list(input())
    length = len(word)
    i = 0
    j = length - 1
    count = 1
    while i < length//2:
        if word[i] == word[j]:
            i += 1
            j -= 1
            continue
        if another_loop(word, i, j-1) or another_loop(word, i+1, j):
            print(1)
            break
        else:
            print(2)
            break
    else:
        print(0)

