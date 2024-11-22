def get_inputs():
	N = int(input())
	accum_scores = [[0] * (N+1) for _ in range(2)]
	for i in range(1, N+1):
		C, P = map(int, input().split())
		accum_scores[C-1][i] = accum_scores[C-1][i-1] + P
		for c in [0, 1]:
			if c != C-1:
				accum_scores[c][i] = accum_scores[c][i-1]
	return N, accum_scores

def solve():
	N, accum_scores = get_inputs()
	Q = int(input())
	for q in range(Q):
		l, r = map(int, input().split())
		A = accum_scores[0][r] - accum_scores[0][l-1]
		B = accum_scores[1][r] - accum_scores[1][l-1]
		print(A, B)

solve()