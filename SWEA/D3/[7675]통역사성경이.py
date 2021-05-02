def is_possible(word):
    if word.isalpha():
        if len(word) == 1:
            return word.isupper()
        return word[0].isupper() and word[1:].islower()
    return False

for t in range(1, int(input())+1):
    n = int(input())
    words = input().split()
    result = [0] * n
    i = 0
    flag = False
    for word in words:
        if word[-1] in '.?!':
            word = word.rstrip(word[-1])
            flag = True
        if is_possible(word):
            result[i] += 1
        if flag:
            i += 1
            flag = False
    print(f'#{t}', *result)
