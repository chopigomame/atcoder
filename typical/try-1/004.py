def getInputs():
	H, W = map(int, input().split())
	As = []
	for _ in range(H):
		As.append(list(map(int, input().split())))
	return H, W, As

def solve():
	H, W, As = getInputs()

	rowSums = []
	for h in range(H):
		rowSums.append(sum(As[h]))
	columnSums = []
	for w in range(W):
		columnSums.append(sum([As[h][w] for h in range(H)]))
	
	for h in range(H):
		ans_h = []
		for w in range(W):
			ans_h.append(rowSums[h] + columnSums[w] - As[h][w])
		print(*ans_h)

solve()
			