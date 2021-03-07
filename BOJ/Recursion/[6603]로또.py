# 6603. 로또 (실버2)

def lotto(level, pick):
    pick_len = len(pick)
    if pick_len == 6:
        print(*pick)
        return
    if pick_len + (k-level+1) < 6:
        return
    lotto(level+1, pick+[s[level-1]])
    lotto(level+1, pick)

while True:
    k, *s = map(int, input().split())
    if not k:
        break
    lotto(1, [])
    print()
