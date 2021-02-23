# Memoization 이용해서 구현 (중복 계산 줄임)
def attach(n):
    if n > 2 and len(memo) < n: # 붙일 수 있는 길이가 20보다 크게 남아있고, memo에 아직 해당 길이에 대한 정보가 없을 때
        memo.append(attach(n-1) + attach(n-2)*2) # 10짜리 종이 붙였을 때와 20짜리 종이를 붙였을 때를 탐색
    return memo[n-1] # n-1인 이유는 10일 때 정보가 인덱스 0에, 20일 때 정보가 인덱스 1에 있기 때문


for t in range(1, int(input())+1):
    n = int(input()) // 10 # 인덱스 계산을 원활히 하기 위해 10으로 나눈 몫으로 재설정
    memo = [1, 3] # 기존 연산을 저장할 메모 선언.
    # 초기값으로 "n이 10만큼 남았을 때 경우의 수 1개", "n이 20만큼 남았을 때 경우의 수 3개" 를 설정
    print('#%s %s' % (t, attach(n)))
