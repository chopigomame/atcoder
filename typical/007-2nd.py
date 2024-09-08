import bisect
def getInputs():
	N = int(input())
	As = list(map(int, input().split()))
	Q = int(input())
	Bs = []
	for q in range(Q):
		Bs.append(int(input()))
	return N, Q, As, Bs

def solve():
	N, Q, As, Bs = getInputs()

	As.sort()
	As.append(float("inf"))

	for b in Bs:
		i = bisect.bisect_left(As, b)
		optimal = min([abs(As[i]-b), abs(As[i-1]-b)])
		print(optimal)

solve()