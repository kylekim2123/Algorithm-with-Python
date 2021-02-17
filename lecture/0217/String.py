for _ in range(1, 11):
    t = int(input())
    target, sentence = input(), input()
    count = 0
    # 문자열의 처음부터 끝(문자열 길이 - 타겟 길이 + 1)까지 반복하면서 일일이 비교
    for i in range(len(sentence)-len(target)+1):
        for j in range(len(target)):
            if sentence[i+j] != target[j]:
                break # 하나라도 다르면 break
        else:
            count += 1 # break가 되지 않았다는 것은 일치한다는 뜻이므로 count + 1
    print('#%s %s' % (t, count))
