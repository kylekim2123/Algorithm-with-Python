# 1063. 킹 (실버4)

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1),
}

k, s, n = input().split()
kx, ky = 8 - int(k[1]), ord(k[0]) - 65  # king x, y
sx, sy = 8 - int(s[1]), ord(s[0]) - 65  # stone x, y

for _ in range(int(n)):
    dx, dy = directions[input()]

    nkx, nky = kx + dx, ky + dy
    if 0 <= nkx < 8 and 0 <= nky < 8:
        if nkx == sx and nky == sy:
            nsx, nsy = sx + dx, sy + dy
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                kx, ky, sx, sy = nkx, nky, nsx, nsy
        else:
            kx, ky = nkx, nky

print(chr(ky + 65) + str(8 - kx))  # king
print(chr(sy + 65) + str(8 - sx))  # stone
