def getInputs():
	N = input()
	As = [int(e) for e in input().split()]
	return As

As = getInputs()
As.sort(reverse=True)

Alice = []
Bob = []
counter = 0
while(len(As)>0):
	if counter %2 == 0:
		Alice.append(As.pop(0))
	else:
		Bob.append(As.pop(0))
	counter += 1

print(sum(Alice) - sum(Bob))