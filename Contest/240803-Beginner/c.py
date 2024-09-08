import bisect

def getInputs():
	N, M = map(int, input().split())
	As = list(map(int, input().split()))
	return N, M, As

def binarySearch(M, As):
	def is_ok(x, As, M):
		summ = 0
		for a in As:
			if x > a:
				summ += a
			else:
				summ += x
		return summ <= M
	ok = 0
	ng = M + 1
	while(abs(ok - ng) > 1):
		mid = (ok + ng) // 2
		if is_ok(mid, As, M):
			ok = mid
		else:
			ng = mid
	return ok

def solve(M, As):
	if sum(As) <= M:
		print("infinite")
		return
	As.sort()
	x = binarySearch(M, As)
	print(x)

N, M, As = getInputs()
solve(M, As)