# 2941. 크로아티아 알파벳 (실버5)

word = input()
changes = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in changes:
    while change in word:
        word = word.replace(change, ".")
print(len(word))
