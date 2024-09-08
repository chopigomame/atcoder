import sys
sys.setrecursionlimit(100000)

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
	def dfs(i, currSum):
		if currSum %2 == 0:
			colors[i] = 0
		else:
			colors[i] = 1
		for j, w in graph[i]:
			if colors[j] == -1:
				dfs(j, currSum + w)
	dfs(0, 0)
	for color in colors:
		print(color)

N, graph = getInputs()
solve(graph)
			