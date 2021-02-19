# 10761. 신뢰

for t in range(1, int(input())+1):
    controls = list(input().split())
    second = 0 # 최소 시간
    robots = {'O': [1, 0], 'B': [1, 0]} # [시작위치(버튼1), 로봇이 행동을 마쳤을 때의 second]

    for i in range(1, len(controls)-1, 2):
        name = controls[i] # 오렌지와 블루
        button = int(controls[i+1]) # 버튼 위치

        # ㅣ가야하는 버튼의 위치 - 로봇의 현재 위치ㅣ -> 즉 로봇이 움직여야 하는 거리(거리는 곧 시간과 같다)
        distance = abs(button - robots[name][0])

        # (전체 second - 자기 자신의 직전 행동을 마쳤을 때의 second) -> 다른 로봇이 행동한 second
        other_robot_sec = second - robots[name][1]

        # 예를 들어, 첫번째 테스트 케이스에서 B가 4번 버튼을 누르려면 2에서 4로 이동해야하므로 distance가 2이다.
        # 이때 other_robot_sec은 B 2와 B 4 사이에 위치한 O의 행동들이 걸린 시간을 의미한다. 즉 3초
        # 이 3초가 나오는 이유는 B 4 시점에서 second는 5이고, robots[name][1]은 B의 직전 행동인 B 2를 마쳤을 때 2초가 걸렸으므로 2이다.
        # 따라서 5에서 2를 뺀 3이 되는 것이다. 이 3은 B 2와 B 4 사이에서 O가 "버튼1을 누르고(1초) + 버튼2로 이동하고 누른다(2초)" 를 의미한다.

        # 아래 if else 문을 보면, B 4 명령에서 B가 2에서 4로 이동하기 위해서는 2만큼 이동해야하는데, 이는 거리이자 소요 시간과 같다. (거리2 = 2초)
        # 즉 "B 2와 B 4 사이의 O가 행동한 시간(other_robot_sec) >= B가 움직여야 하는 거리(2)" 라면, B는 이미 O가 행동하는 동안 버튼4로 이동을 완료했으므로
        # second에는 B가 버튼4를 누르는 1초만 더해주면 된다.
        
        # 반면 "B 2와 B 4 사이의 O가 행동한 시간(other_robot_sec) < B가 움직여야 하는 거리(2)" 라면, B는 O가 행동하는 동안에도 버튼 4로 이동을 못한 것이므로
        # second에는 B가 버튼4로 이동할 수 있도록 추가 시간을 더하고(distance-other_robot_sec), 버튼을 누르는 시간(1초) 까지 더해야한다.
        second += 1  if distance <= other_robot_sec else (distance-other_robot_sec+1)

        robots[name][0] = button # 그리고 버튼으로 이동했으므로 로봇의 위치를 갱신
        robots[name][1] = second # 행동이 끝났으므로 현재 행동까지 걸린 시간을 갱신

    print(f'#{t} {second}')
