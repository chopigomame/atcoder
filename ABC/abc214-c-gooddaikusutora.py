import heapq
def getInputs():
	N = int(input())
	Ss = list(map(int, input().split()))
	Ts = list(map(int, input().split()))
	return N, Ss, Ts

def solve(N, Ss, Ts):
	INF = float("inf")
	Ds = [INF for _ in range(N+1)]
	Ds[0] = 0
	DsHeap = [[0, 0]]

	while DsHeap:
		d, cv = heapq.heappop(DsHeap)
		
		if Ds[cv] < d: continue
		if cv == 0:
			edges = [[i+1, t] for i, t in enumerate(Ts)]
		else:
			if cv < N:
				edges = [[cv+1, Ss[cv-1]]]
			else:
				edges = [[1, Ss[cv-1]]]
		for edge in edges:
			if Ds[edge[0]]> d + edge[1]:
				Ds[edge[0]] = d + edge[1]
				heapq.heappush(DsHeap, [d + edge[1], edge[0]])
	print(*Ds[1:], sep="\n")

N, Ss, Ts = getInputs()
solve(N, Ss, Ts)
