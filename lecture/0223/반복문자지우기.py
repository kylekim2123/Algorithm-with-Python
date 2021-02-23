def erase(word, start):
    for i in range(start, len(word)-1): # 앞에 검사한 만큼은 제외하고, 반복문자가 나왔던 곳 바로 앞에서 부터 다시 탐색
        if word[i] == word[i+1]: # 반복문자가 등장하면,
            start = i-1 if i > 0 else 0 # 맨앞에서 등장했으면 start는 0으로, 아니라면 바로 직전 인덱스로 지정
            return erase(word.replace(word[i]+word[i+1], ''), start) # 반복문자를 모두 지우고 재귀
    return len(word) # 더이상 반복문자가 없으면 길이 반환


for t in range(1, int(input())+1):
    word = input()
    print('#%s %s' % (t, erase(word, 0)))
