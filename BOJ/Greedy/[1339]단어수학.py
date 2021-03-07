# 1339. 단어 수학 (골드4)

n = int(input())
alphabet = {}
for _ in range(n):
    word = input()
    x = len(word)-1
    for char in word:
        alphabet[char] = alphabet.get(char, 0) + (10**x)
        x -= 1

result = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
total, num = 0, 9
for r in result:
    total += (r[1]*num)
    num -= 1
print(total)