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
	DP = [0 for _ in range(3)]
	for i in range(N):
		currDP = [0 for _ in range(3)]
		a = S[i]
		for j in range(3):
			takahashiScore_ij = calcTakahashiScore(j, a)
			if takahashiScore_ij ==  -1:
				currDP[j] = 0
			else:
				currDP[j] = max([DP[k] for k in range(3) if k != j]) + takahashiScore_ij
		DP = currDP
	print(max(DP))

N, Slist = getInputs()
solve(N, Slist)