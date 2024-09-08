import math, sys
sys.setrecursionlimit(10**8)

def get_inputs():
	N = int(input())
	S = input()
	return N, S


def solve():
	N, S = get_inputs()
	DP = [[0]*8 for _ in range(N+1)] # DP[i][j]: i文字目までの取捨をして、atcoder のj文字目まで一致する方法の数
	for i in range(N+1):
		DP[i][0] += 1
	atc = list("atcoder")

	for i in range(1, N+1):
		for j in range(1, 8):
			DP[i][j] += DP[i-1][j]
			if S[i-1]==atc[j-1]:
				DP[i][j] += DP[i-1][j-1]
	print(DP[N][7] % (10**9 + 7))

solve()