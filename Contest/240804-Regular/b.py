def getCase():
	S = input()
	X = list(map(int, input()))
	Y = list(map(int, input()))
	return S, X, Y

def getComponent(S):
	lenS = len(S)
	for i in range(lenS//2):
		if lenS % (i+1) != 0:
			continue
		comp = S[:i+1]
		if comp * (lenS//(i+1)) == S:
			return comp
	return S

def func(S, T, Z):
	ret = ""
	for z in Z:
		if z == 0:
			ret += S
		else:
			ret += T
	return ret

		

def solve():
	def binarySearch():
		def isOK(i):
			componentI = sComponent * i
			tempXStringReplaced = tempXString.replace("R", componentI)
			tempYStringReplaced = tempYString.replace("R", componentI)
			if sum(X) >= sum(Y):
				return len(tempXStringReplaced) <= len(tempYStringReplaced)
			if sum(Y) >= sum(X):
				return len(tempYStringReplaced) <= len(tempXStringReplaced)
		ng = 1e5
		ok = 0
		while(abs(ng - ok) > 1):
			mid = int((ng + ok) // 2)
			if isOK(mid):
				ok = mid
			else:
				ng = mid
		return ok
	
	T = int(input())
	for _ in range(T):
		S, X, Y = getCase()
		sComponent = getComponent(S)
		tempXString = func(S, "R", X)
		tempYString = func(S, "R", Y)
		repeat = binarySearch()
		nS = sComponent * repeat
		tempXStringReplaced = tempXString.replace("R", nS)
		tempYStringReplaced = tempYString.replace("R", nS)
		if tempXStringReplaced == tempYStringReplaced:
			print("Yes")
		else:
			print("No")

solve()