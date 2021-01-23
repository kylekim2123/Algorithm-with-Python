# 1940. 가랏! RC카!

results = list()
for t in range(1, int(input()) + 1):
    distance = 0
    speed = 0
    for n in range(int(input())):
        commands = list(map(int, input().split()))
        if commands[0] == 1:
            speed += commands[1]
        elif commands[0] == 2:
            if speed < commands[1]:
                speed = 0
            else:
                speed -= commands[1]
        distance += speed
    results.append(f'#{t} {distance}')

for result in results:
    print(result)