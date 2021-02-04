# 8741. 두문자어

for t in range(1, int(input())+1):
    sentence = input()
    sentence.title()
    acronym_list = [word[0].upper() for word in sentence.split()]
    acronym = ''.join(acronym_list)
    print(f'#{t} {acronym}')