#미로 탈출(BFS)
from collections import deque

n,m = map(int,input().split())
graph = []

for i in range(n):
	graph.append(list(map(int,input())))


#이동 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	queue = deque()
	queue.append((x,y))
	while queue:
		x,y = queue.popleft()
		# 4방향으로 위치 확인
		for i in range(4):
			nx = x +dx[i]
			ny = y + dy[i]
			#미로 찾기 공간 범위를 벗어나는 경우
			if nx < 0 or ny <0 or nx >=n or ny >=m:
				continue
			# 벽인 경우
			if graph[nx][ny] == 0:
				continue
			# 처음 방문한 경우
			if graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1
				queue.append((nx,ny))
	#목적지까지의 최단거리 반환
	return graph[n-1][m-1]



print(bfs(0,0))
