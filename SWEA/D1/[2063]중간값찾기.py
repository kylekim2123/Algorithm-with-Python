# 2063. 중간값 찾기

length = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[length // 2])