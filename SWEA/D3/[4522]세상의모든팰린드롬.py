# 4522. 세상의 모든 팰린드롬

for  t in range(1, int(input())+1):
    word = input()
    i, j = 0, len(word)-1
    while i < j:
        if word[i] == word[j] or word[i] == '?' or word[j] == '?':
            i += 1
            j -= 1
            continue
        print(f'#{t} Not exist')
        break
    else:
        print(f'#{t} Exist')
    