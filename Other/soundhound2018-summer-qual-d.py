import heapq

def getInputs():
	n, m, s, t = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(m):
		u, v, a, b = map(int, input().split())
		graph[u-1].append([v-1, a, b]) # to, costYen, costSnuuk
		graph[v-1].append([u-1, a, b])
	return n, m, s-1, t-1, graph 

def diastra(start, graph, currency):
	INF = float("inf")
	ds = [INF for _ in range(len(graph))]
	ds[start] = 0
	dsQueue = [[0, start]] # distance_from_start, node_index

	while dsQueue:
		d, cv = heapq.heappop(dsQueue)
		if d > ds[cv]: continue
		
		for edge in graph[cv]:
			to = edge[0]
			if currency == "yen": cost=edge[1]
			else: cost=edge[2]
			if ds[to] > ds[cv] + cost:
				ds[to] = ds[cv] + cost
				heapq.heappush(dsQueue, [ds[to], to])
	return ds


def solve(n, s, t, graph):
	yenCostsFromStart = diastra(s, graph, "yen")
	snuukCostsFromGoal = diastra(t, graph, "snuuk")
	totalCostsForEveryExchange = [yenCostsFromStart[i] + snuukCostsFromGoal[i] for i in range(n)]
	tempMinCost = float("inf")
	resides = []
	shojikin = 10**15
	for i in range(n-1, -1, -1):
		tempMinCost = min(totalCostsForEveryExchange[i], tempMinCost)
		resides.append(shojikin - tempMinCost)
	print(*resides[::-1], sep="\n")

n, m, s, t, graph = getInputs()
solve(n, s, t, graph)