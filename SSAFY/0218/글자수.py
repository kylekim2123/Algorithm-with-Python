for t in range(1, int(input())+1):
    str1, str2 = set(input()), input() # str1을 set으로 만들어서 중복 제거
    count = dict.fromkeys(str1, 0) # str1의 문자를 key로 딕셔너리 생성. value는 0으로 초기화
    for x in str2:
        if x in str1:
            count[x] += 1 # str2를 돌면서 str1에 있는 문자가 있으면 count + 1
    print('#%s %s' % (t, max(count.values())))