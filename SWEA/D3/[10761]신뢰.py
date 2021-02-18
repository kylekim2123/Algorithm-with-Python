# 10761. 신뢰

for t in range(1, int(input())+1):
    controls = list(input().split())
    robots = {'O': [1, 0], 'B': [1, 0]}
    second = 0
    for i in range(1, len(controls)-1, 2):
        name = controls[i]
        button = int(controls[i+1])
        distance = abs(button - robots[name][0])
        robot_sec = second - robots[name][1]
        second += 1  if distance <= robot_sec else (distance-robot_sec+1)
        robots[name][0] = button
        robots[name][1] = second
    print(f'#{t} {second}')
