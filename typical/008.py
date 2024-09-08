import math, sys
sys.setrecursionlimit(10**8)

def get_inputs():
	N = int(input())
	S = input()
	return N, S

def create_next(N, S):
	nex = [[N]*7 for _ in range(N+1)]
	chars = list("atcoder")
	for i in range(N-1, -1, -1):
		for k in range(7):
			nex[i][k] = nex[i+1][k]
		for k, char in enumerate(chars):
			if S[i] == char:
				nex[i][k] = i
				break
	return nex


	

def solve():
	def dfs(i, j):
		if i == N:
			return 0
		if DP[i][j] != -1:
			return DP[i][j]
		next_j_index = nex[i+1][j]
		count = dfs(next_j_index, j) + 1 # S[i:]に文字種jが含まれている数 = 次のjからいくつ含まれてるか + 自分自身の1
		DP[i][j] = count
		return count

	def dfs2(i, j):
		count = 0
		while(True):
			if i == N:
				break
			if j != 6:
				next_j1_index = nex[i][j+1]
				if next_j1_index != N:
					count += dfs2(next_j1_index, j+1)
			else:
				count += 1
			i = nex[i+1][j]
		return count
			

	N, S = get_inputs()
	nex = create_next(N, S)

	DP = [[-1]*7 for _ in range(N)] # DP[i][j]: S[i:]に、文字種jがいくつ含まれているか の配列
	for j in range(7):
		dfs(nex[0][j], j)
	count = dfs2(nex[0][0], 0)
	print(count % (10**9+7))


solve()