def getInputs():
	Y = int(input())
	return Y

def solve(Y):
	if Y%4 != 0:
		print(365)
	elif Y%4 == 0 and Y%100 != 0:
		print(366)
	elif Y%100==0 and Y%400 != 0:
		print(365)
	elif Y%400 == 0:
		print(366)

Y = getInputs()
solve(Y)