import bisect
def getInputs():
	N = int(input())
	As = list(map(int, input().split()))
	Q = int(input())
	Bs = []
	for q in range(Q):
		Bs.append([q, int(input())])
	return N, Q, As, Bs

def solve():
	N, Q, As, Bs = getInputs()

	As.sort()
	Bs.sort(key=lambda x:x[1])
	diffs = [-1 for _ in range(Q)]

	prev_optimal_index = 0
	for bl in Bs:
		b = bl[1]
		i = bisect.bisect_left(As[prev_optimal_index:], b)
		i += prev_optimal_index
		if i == N:
			optimal = [N-1, abs(As[N-1]-b)]
		elif i == 0:
			optimal = [0, abs(As[0]-b)]
		else:
			optimal = min([[i, abs(As[i]-b)], [i-1, abs(As[i-1]-b)]], key=lambda x:x[1])
		prev_optimal_index = optimal[0]
		diffs[bl[0]] = optimal[1]
	print(*diffs, sep="\n")

solve()