import bisect
def getInputs():
	N, K = map(int, input().split())
	S = input()
	return N, K, S


def solve():
	N, K, S = getInputs()
	partial = list("{" * K)

	for n in range(N):
		S_reside_num = N - n
		K_start = max(0, K - S_reside_num)
		k = bisect.bisect_right(partial[K_start:], S[n])
		k += K_start
		if k >= K:
			continue
		partial[k] = S[n]
		partial[k+1:] = "{" * (K - (k+1))
	print("".join(partial))

solve()