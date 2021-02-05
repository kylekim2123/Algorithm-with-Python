# 1316. 그룹 단어 체커

group_word = 0
for _ in range(int(input())):
    word = list(input())
    while word:
        i = 0
        if (word.count(word[i]) == 1) or (word[i] == word[i+1]):
            word.remove(word[i])
            continue
        break
    else:
        group_word += 1
print(group_word)