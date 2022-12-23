#위상 정렬 소스코드

from collections import deque

#노드, 간선 개수
v,e = map(int,input().split())
#모든 노드 진입차수 1로 초기화
indegree = [0] * (v+1)
#연결 리스트 초기화
graph = [ [] for i in range(v+1)]

#간선 정보 입력받기
for _ in range(e):
	a,b = map(int,input().split())
	graph[a].append(b)
	indegree[b] += 1

def topology_sort():
	result = []
	q = deque()

	for i in range(1,v+1):
		if indegree[i] == 0:
			q.append(i)
	
	while q:
		now = q.popleft()
		result.append(now)
		#해당 원소와 연결된 노드들의 진입차수 1뺴기
		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	for i in result:
		print(i,end = ' ')



topology_sort()
