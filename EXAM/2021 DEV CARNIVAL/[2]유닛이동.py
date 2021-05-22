# 2번문제 : 유닛 이동

from collections import deque

def bfs(x1, y1, x2, y2):
	visited1 = [[0]*n for _ in range(n)]
	visited2 = [[0]*n for _ in range(n)]
	visited1[x1][y1] = visited2[x2][y2] = 1
	queue1 = deque([(x1, y1)])
	queue2 = deque([(x2, y2)])
	start1 = start2 = True
	end1 = end2 = False
	result = []
	
	while queue1 or queue2:
		if queue1:
			x1, y1 = queue1.popleft()
		else:
			start1 = False
		if queue2:
			x2, y2 = queue2.popleft()
		else:
			start2 = False
		
		for i in range(4):
			if start1 and not end1:
				nx1, ny1 = x1+dx[i], y1+dy[i]
				if 0 <= nx1 < n and 0 <= ny1 < n and not visited1[nx1][ny1] and grid[nx1][ny1] != 'X':
					visited1[nx1][ny1] = visited1[x1][y1] + 1
					if grid[nx1][ny1] == 'D':
						result.append(visited1[nx1][ny1])
						end1 = True
					queue1.append((nx1, ny1))
			
			if start2 and not end2:
				nx2, ny2 = x2+dx[i], y2+dy[i]
				if 0 <= nx2 < n and 0 <= ny2 < n and not visited2[nx2][ny2] and grid[nx2][ny2] != 'X':
					visited2[nx2][ny2] = visited2[x2][y2] + 1
					if grid[nx2][ny2] == 'D':
						result.append(visited2[nx2][ny2])
						end2 = True
					queue2.append((nx2, ny2))

	return max(result)-1 if (end1 and end2) else -1
			

n = int(input())
grid = [list(input()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
print(bfs(*map(int, input().split())))