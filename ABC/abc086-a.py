from typing import Tuple
def getInput() -> Tuple[int, int]:
	a, b = input().split()
	return int(a), int(b)

def judgeOddEven(a, b):
	return a*b % 2 == 0

a, b = getInput()
if judgeOddEven(a, b):
	print("Even")
else:
	print("Odd")
	