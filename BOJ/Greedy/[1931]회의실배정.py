# 1931. 회의실 배정 (실버2)

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
last_end = 0
max_meeting_counts = 0

for start, end in meetings:
    if last_end <= start:
        max_meeting_counts += 1
        last_end = end

print(max_meeting_counts)
