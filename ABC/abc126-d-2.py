from collections import deque

def getInputs():
	N = int(input())
	graph = [[] for _ in range(N)]
	for _ in range(N-1):
		u, v, w = map(int, input().split())
		graph[u-1].append((v-1, w))
		graph[v-1].append((u-1, w))
	return N, graph

def solve(graph):
	colors = [-1 for _ in range(N)]
	colors[0] = 0
	que = deque([0])
	while que:
		cv = que.popleft()
		for nv, w in graph[cv]:
			if colors[nv] != -1:
				continue
			if w % 2 == 0:
				colors[nv] = colors[cv]
			else:
				colors[nv] = colors[cv] ^ 1
			que.append(nv)
	for color in colors:
		print(color)

N, graph = getInputs()
solve(graph)
			