def get_inputs():
	N = int(input())
	hs = list(map(int, input().split()))
	return N, hs

def solve():
	N, hs = get_inputs()
	INF = 10**9
	DP = [INF] * N
	DP[0] = 0

	for i in range(N-1): # 足場iからの移動によるコストの計算をする
		DP[i+1] = min(DP[i+1], DP[i] + abs(hs[i] - hs[i+1]))
		if i+2 < N:
			DP[i+2] = min(DP[i+2], DP[i] + abs(hs[i] - hs[i+2]))
	print(DP[N-1])


solve()