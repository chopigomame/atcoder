from typing import Tuple, List
def getInputs() -> Tuple[int, int, int, int]:
	A = int(input())
	B = int(input())
	C = int(input())
	X = int(input())
	return A, B, C, X

A, B, C, X = getInputs()

count = 0
for a in range(A+1):
	for b in range(B+1):
		for c in range(C+1):
			if X == a*500 + b*100 + c*50:
				count += 1
print(count)