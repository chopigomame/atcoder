import heapq
def getInputs():
	N = int(input())
	Ss = list(map(int, input().split()))
	Ts = list(map(int, input().split()))
	graph = [[[cost, i+1] for (i, cost) in enumerate(Ts)]] # index = 0, means Takahashi
	for i, S in enumerate(Ss[:-1]):
		to = i + 2
		graph.append([[S, to]]) # index in [1, N], means Sunuke
	graph.append([[Ss[-1], 1]])
	return N, graph


def diastra(s, graph):
	"""
	Description
		s から 各ノード (0 - N) への最短距離 Ds を返す
	"""
	INF = float("inf")
	Ds = [INF for _ in graph]
	Ds[s] = 0
	que = [[Ds[0], 0]] # distance, index
	while que:
		d, i = heapq.heappop(que)
		if d > Ds[i]:
			continue
		for e in graph[i]:
			cost, to = e
			if Ds[to] > Ds[i] + cost:
				Ds[to] = Ds[i] + cost
				heapq.heappush(que, [Ds[to], to])
	return Ds
	

def solve():
	N, graph = getInputs()
	Ds = diastra(0, graph)
	print(*Ds[1:], sep="\n")

solve()