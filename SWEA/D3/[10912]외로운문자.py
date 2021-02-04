# 10912. 외로운 문자

for t in range(1, int(input())+1):
    sentence = input()
    result = ''
    for digit in sentence:
        count = sentence.count(digit)
        if (count == 1) or ((count % 2) and (digit not in result)):
            result += digit
    
    if result:
        sorted_result = ''.join(sorted(list(result)))
        print(f'#{t} {sorted_result}')
    else:
        print(f'#{t} Good')
            