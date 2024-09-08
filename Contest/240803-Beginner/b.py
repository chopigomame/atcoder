import bisect
def getInputs():
	N = int(input())
	As = list(map(int, input().split()))
	return N, As

def solve(As):
	AsWithIndex = [[i, a] for (i,a) in enumerate(As)]
	AsWithIndex.sort(key=lambda x:x[1])
	maxI = bisect.bisect_left(AsWithIndex, AsWithIndex[-1][1], key=lambda x:x[1])
	print(AsWithIndex[maxI-1][0] + 1)

N, As = getInputs()
solve(As)