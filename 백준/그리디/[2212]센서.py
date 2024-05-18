# 2212. 센서 (골드5)
n = int(input())
k = int(input())
sensors = sorted(list(set(map(int, input().split()))))

if len(sensors) <= k:
    print(0)
else:
    distance = []
    for i in range(1, len(sensors)):
        distance.append(sensors[i]-sensors[i-1])
    distance.sort(reverse=True)
    print(sum(distance[k-1:]))

# 1. 센서들을 중복없이 정렬한다.
# 2. 센서보다 기지국이 많으면 안된다.
# 3. 각 센서간의 거리 차이로 이루어진 배열을 만든다.
# 4. 거리 차이 배열을 내림차순 정렬한다.
# 5. 거리 차이 배열에서 큰 값들을 기준으로 기지국이 나눠진다.
# 6. 따라서 k-1개 만큼 맨 앞에서 빼고 나머지의 총합이 바로 답!