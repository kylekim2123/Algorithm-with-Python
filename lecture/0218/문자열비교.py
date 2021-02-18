for t in range(1, int(input())+1):
    str1, str2 = input(), input()
    len1, len2 = len(str1), len(str2)
    for i in range(len2-len1+1): # 고지식한 패턴 매칭
        for j in range(len1):
            if str2[i+j] != str1[j]:
                break # 문자 하나라도 다르면 탈출
        else:
            print('#%s %s' % (t, 1))
            break
    else:
        print('#%s %s' % (t, 0))
