from typing import Tuple, List
from itertools import combinations

def getInputs() -> Tuple[int, int, int]:
	N, A, B = [int(e) for e in input().split()]
	return N, A, B

def getDigits(number):
	digits = 1
	while(True):
		number /= 10
		if number < 1:
			break
		digits += 1
	return digits	

def getPatterns(digit, patterns): # 再帰で作れた。digit桁の数値を構成する数値種の全組み合わせを生成する関数。
	if digit == 0:
		return patterns
	if not patterns:
		for n in range(1, 10):
			patterns.append([n])
		return getPatterns(digit-1, patterns)
	else:
		newPatterns = []
		for pattern in patterns:
			prevNumber = pattern[-1]
			for n in range(prevNumber+1):
				newPattern = pattern + [n]
				newPatterns.append(newPattern)
		return getPatterns(digit-1, newPatterns)

def callPermNums(pattern:list):
	pass
	
			
def calcPatternsSum(number, A, B):
	digits = getDigits(number)
	for d in range(1, digits+1):
		patterns = 10
		


N, A, B = getInputs()
sum()

