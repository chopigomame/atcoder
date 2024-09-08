def get_inputs():
	N, K = map(int, input().split())
	hs = list(map(int, input().split()))
	return N, K, hs

def solve():
	N, K, hs = get_inputs()
	INF = 10**18
	DP = [INF] * N
	DP[0] = 0

	for i in range(N-1): # 足場iからの移動によるコストの計算をする
		for k in range(1, K+1):
			if i+k < N:
				DP[i+k] = min(DP[i+k], DP[i] + abs(hs[i] - hs[i+k]))
	print(DP[-1])


solve()