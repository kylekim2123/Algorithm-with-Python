# 재귀
def subset(index):
    if index == SIZE: # 원소의 끝까지 봤다면 그만 본다
        if sum(check) == n and k == sum([x+1 for x in range(SIZE) if check[x]]):
            # sum(check) : 부분집합을 몇 개 뽑았는가? n개 만큼 뽑으면 True
            # sum([x+1 for x in range(SIZE) if check[x]]) : 어차피 A가 1~12 이므로, "check 인덱스 + 1"을 하면 1~12 사이의 숫자가 나온다.
            global count
            count += 1
        return
    check[index] = 0 # 해당 원소를 뽑지 않음
    subset(index+1) # 다음 부분집합 탐색
    check[index] = 1 # 해당 원소를 뽑음
    subset(index+1) # 다음 부분집합 탐색


SIZE = 12
for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    check, count = [0]*SIZE, 0
    subset(0)
    print('#%s %s' % (t, count))
