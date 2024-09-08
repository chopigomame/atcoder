def getInputs():
	N, Y = [int(e) for e in input().split()]
	return N, Y

N, Y = getInputs()

found = False
for i in range(N+1):
	if found:
		break
	curr = 10000 * i
	if curr > Y:
		continue
	for j in range(N-i+1):
		k = N - (i + j)
		if curr + 5000 * j + 1000 * k == Y:
			print(i, j, k)
			found = True

if not found:
	print(-1, -1, -1)