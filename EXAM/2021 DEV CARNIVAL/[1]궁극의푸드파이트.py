# 1번문제. 궁극의 푸드 파이트

n, k = map(int, input().split())
a = list(map(int, input().split()))
k -= 1
length_a = len(a)
result = []
while any(a):
	if not a[k]:
		k += 1
		if k >= length_a:
			k = 0
		continue
	a[k] -= 1
	if not a[k]:
		result.append(k+1)
	k += 1
	if k >= length_a:
		k = 0
print(*result)