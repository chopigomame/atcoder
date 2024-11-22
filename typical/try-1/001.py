def getInputs():
	N, L = map(int, input().split())
	K = int(input())
	As = list(map(int, input().split()))
	return N, L, K, As

def solve(N, L, K, As):
	def isOk(x):
		curr = 0
		currK = 0
		prevA = 0
		for i, a in enumerate(As):
			curr += As[i] - prevA
			prevA = As[i]
			if curr >= x:
				curr = 0
				currK += 1
				if currK == K:
					if L - As[i] >= x:
						return True
					else:
						return False
		return False
			
	ok = 0
	ng = L + 1

	while(abs(ok - ng) > 1):
		mid = (ng + ok) / 2
		if isOk(mid):
			ok = mid
		else:
			ng = mid
	print(int(ok)+1)
		
solve(*getInputs())