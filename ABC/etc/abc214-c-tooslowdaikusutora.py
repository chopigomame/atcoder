def getInputs():
	N = int(input())
	Ss = list(map(int, input().split()))
	Ts = list(map(int, input().split()))
	return N, Ss, Ts

def solve(N, Ss, Ts):
	INF = float("inf")
	Ds = [INF for _ in range(N+1)]
	Ds[0] = 0
	unuseds = [i for i in range(N+1)]

	while True:
		cv = -1
		for i, unused in enumerate(unuseds):
			if cv == -1 or Ds[cv] > Ds[unused]:
				cv = unused
				del_i = i
		if cv == -1:
			break
		del unuseds[del_i]
		
		if cv == 0:
			edges = [[i+1, t] for i, t in enumerate(Ts)]
		else:
			if cv < N:
				edges = [[cv+1, Ss[cv-1]]]
			else:
				edges = [[1, Ss[cv-1]]]
		
		for edge in edges:
			if Ds[edge[0]] > Ds[cv] + edge[1]:
				Ds[edge[0]] = Ds[cv] + edge[1]
	print(*Ds[1:], sep="\n")

N, Ss, Ts = getInputs()
solve(N, Ss, Ts)
