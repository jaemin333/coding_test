#다익스트라 간단한 ver
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값

#노드 , 간선의 개수 
n,m = map(int,input().split())
#시작 노드 
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for i in range(n+1)]
#방문 정보
visited = [False] * (n+1)
#최단 거리 테이블
distance = [INF] * (n+1)

#간선 정보 입력받기
for _ in range(m):
	a,b,c = map(int,input().split())
	#a번에서 b번 노드로 가는 비용은 c
	graph[a].append((b,c))

#방문하지 않은 노드 중, 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
	min_value = INF
	index = 0
	for i in range(1,n+1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index


def dijkstra(start):
	distance[start] = 0
	visited[start] = True
	for j in graph[start]:
		distance[j[0]] = j[1]
	for i in range(n-1):
		now = get_smallest_node()
		visited[now] = True
		for j in graph[now]:
			cost = distance[now] + j[1]
			if cost < distance[j[0]]:
				distance[j[0]] = cost


dijkstra(start)

for i in range(1,n+1):
	if distance[i] == INF:
		print("INFINITY")
	else:
		print(distance[i])
