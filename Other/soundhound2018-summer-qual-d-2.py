import heapq

def getInputs():
	n, m, s, t = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v, a, b = map(int, input().split())
		graph[u-1].append([v-1, a, b]) # to, costYen, costSnuuk
		graph[v-1].append([u-1, a, b])
	return n, m, s-1, t-1, graph 

def diastra():