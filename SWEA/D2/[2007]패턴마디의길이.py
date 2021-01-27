# 2007. 패턴 마디의 길이

for t in range(1, int(input()) + 1):
    word = input()
    pattern_length = 0 # 패턴 마디의 길이를 담을 변수 (최종 결과)

    for i in range(1, 11): # 패턴의 길이는 1 ~ 10
        last_index = len(word) - (len(word) % i) # 패턴의 길이에 따라서, 문자열의 어디까지 검사할것인가
        pre_char = word[0:i] # 패턴의 길이에 따른 최초 패턴
        for j in range(0, last_index - i + 1, i): # 패턴을 찾아 나가는데, 패턴의 길이만큼 매번 뛰어넘는다
            now_char = word[j:j+i] # 패턴과 검사할 현재 문자열의 조각
            if pre_char != now_char:
                break # 패턴과 현재 문자열이 다르면 패턴이 잘못되었으므로 다음으로 넘어간다. break
        else:
            pattern_length = len(pre_char) # 패턴과 모든 검사 문자열이 같으면, 패턴이 올바른것이므로 패턴의 길이를 넣는다.
            break # 패턴이 이미 완성되었기 때문에 다른건 볼 필요도 없다.

    print(f'#{t} {pattern_length}') # 결과 출력
