# 4406. 모음이 보이지 않는 사람

for t in range(1, int(input())+1):
    word = list(input())
    for i in range(len(word)):
        if word[i] in {'a', 'e', 'i', 'o', 'u'}:
            word[i] = ''
    print(f'#{t} {"".join(word)}')