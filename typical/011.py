def get_inputs():
	N = int(input())
	DCSs = []
	for _ in range(N):
		D, C, S = map(int, input().split())
		DCSs.append([D,C,S])
	return N, DCSs

def solve():
	N, DCSs = get_inputs()
	DCSs.sort(key = lambda x: x[0])
	D_max = max(DCSs, key=lambda x: x[0])[0]

	DP = [[0]*(D_max+1) for _ in range(N + 1)]
	for i, dcs in enumerate(DCSs, 1):
		d, c, s = dcs
		for j in range(D_max+1):
			if j < c or d < j:
				DP[i][j] = DP[i-1][j]
			else:
				DP[i][j] = max(DP[i-1][j], DP[i-1][j-c] + s)
	print(max(DP[N]))
	
solve()