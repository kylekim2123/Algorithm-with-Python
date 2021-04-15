absolutes = [4, 7, 12]
signs = [True, False, True]
answer = 0

for i, sign in enumerate(signs):
    if sign:
        answer += absolutes[i]
    else:
        answer -= absolutes[i]
print(answer)