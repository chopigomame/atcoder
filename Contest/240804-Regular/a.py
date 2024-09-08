def getCase():
	N = int(input())
	Ps = list(map(int, input().split()))
	return N, Ps

def solve():
	T = int(input())
	for _ in range(T):
		solved = False
		N, case = getCase()
		if tuple(case) == tuple([i+1 for i in range(N)]):
			print(0)
			solved = True
			continue
		else:
			max = -1
			for n in range(N):
				if n+1 == case[n] and case[n] > max:
					print(1)
					solved = True
					break
				if case[n] > max:
					max = case[n]
		if not solved:
			if case[0] == N and case[-1] == 1:
				print(3)
			else:
				print(2)
		
solve()