import sys
sys.setrecursionlimit(int(1e9))

def getInputs():
	N = int(input())
	Slist = list(map(int, list(input().replace("R", "0").replace("P", "1").replace("S", "2"))))
	return N, Slist

def calcTakahashiScore(t, a):
	if t == a:
		return 0
	if (t,a) in ((0, 2), (1, 0), (2, 1)):
		return 1
	else:
		return -1

def solve(N, S):
	def dfs(i, j, accumScore):
		if DP[i][j] != INF:
			return DP[i][j] + accumScore
		currScore = calcTakahashiScore(j, S[i])
		if currScore == -1:
			DP[i][j] = -1
			return -1
		totalScore = accumScore + currScore
		if i == N-1:
			DP[i][j] = totalScore - accumScore
			return totalScore 
		else:
			c = max([dfs(i+1, k, totalScore) for k in range(3) if k!= j])
			DP[i][j] = c - accumScore
			return c
	maxScore = -1
	for k in range(3):
		INF = -float("inf")
		DP = [[INF for _ in range(3)] for _ in range(N)]
		score = dfs(0, k, 0)
		if score > maxScore:
			maxScore = score
	print(maxScore)
		

N, Slist = getInputs()
solve(N, Slist)