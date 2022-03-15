# 1339. 단어수학 (골드4)

n = int(input())
alphabets = {}

for _ in range(n):
    word = input()
    digit = len(word) - 1
    for i in word:
        alphabets[i] = alphabets.get(i, 0) + (10 ** digit)
        digit -= 1

number, total = 9, 0
for value in sorted(alphabets.values(), reverse=True):
    total += value * number
    number -= 1

print(total)
