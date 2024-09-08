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
	maxWin = [0 for _ in range(3)]
	for i in range(N-1, -1, -1):
		a = S[i]
		currMaxWin = []
		for j in range(3):
			takahashiScore_ij = calcTakahashiScore(j, a)
			if takahashiScore_ij ==  -1:
				currMaxWin.append(-1)
				continue
			currMaxWin.append(max([maxWin[k] for k in range(3) if k!=j and maxWin[k] != -1]) + takahashiScore_ij)
		maxWin = currMaxWin
	print(max(maxWin))

N, Slist = getInputs()
solve(N, Slist)