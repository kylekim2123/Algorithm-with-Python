# 2477. 참외밭 (실버5)

k_melon = int(input())
length = []
for _ in range(6):
    d, l = map(int, input().split())
    length.append(l)
w = max(length)
w_idx = length.index(w)
next_w_idx = w_idx+1 if w_idx+1 <7 else 0
h, temp1 = max(length[w_idx-1], length[next_w_idx]), min(length[w_idx-1], length[next_w_idx])
temp1_idx = length.index(temp1)
next_temp_idx = temp1_idx+1 if temp1_idx+1 <7 else 0
temp2 = min(length[temp1_idx-1], length[next_temp_idx])
print(((w*h) - (temp2*(h-temp1))) * k_melon)