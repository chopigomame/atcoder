from typing import Tuple, List
def getInputs() -> Tuple[int, List[int]]:
	N = int(input())
	As = [int(e) for e in input().split()]
	return N, As

N, As = getInputs()
count = 0
dividable = True
while(dividable):
	for i, A in enumerate(As):
		if A % 2 == 0:
			As[i] = A/2
		else:
			dividable = False
			break
	if dividable:
		count += 1
print(count)