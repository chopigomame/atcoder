import bisect

def getInputs():
	N = int(input())
	Ss = []
	Ts = []
	for _ in range(N):
		Ss.append(input())
	M = int(input())
	for _ in range(M):
		Ts.append(input())
	Ss.sort()
	Ts.sort()
	return Ss, Ts

def summarize(wholeList, tgts):
	summary = {}
	for tgt in tgts:
		summary[tgt] = bisect.bisect_right(wholeList, tgt) - bisect.bisect_left(wholeList, tgt)
	return summary
		
	
def solve(Ss, Ts):
	uniqueSs = set(Ss)
	summarySs = summarize(Ss, uniqueSs)
	summaryTs = summarize(Ts, uniqueSs)
	
	yen = 0
	for tgt in uniqueSs:
		currYen = summarySs[tgt] - summaryTs[tgt]
		if currYen > yen:
			yen = currYen
	return yen

Ss, Ts = getInputs()
print(solve(Ss, Ts))