def getInputs():
	N = int(input())
	txys = []
	for _ in range(N):
		t, x, y = [int(e) for e in input().split()]
		txys.append([t, x, y])
	return txys

def canGo(txy1, txy2):
	t1, x1, y1 = txy1
	t2, x2, y2 = txy2
	needTurns = abs(x1 - x2) + abs(y1 - y2)
	ok1 = t2 - t1 >= needTurns
	ok2 = (needTurns - (t2 - t1)) % 2 == 0
	return ok1 and ok2


txys = getInputs()
txys.insert(0, [0, 0, 0])

canGoAll = True
for i in range(len(txys)-1):
	if not canGo(txys[i], txys[i+1]):
		canGoAll = False
		break

if canGoAll:
	print("Yes")
else:
	print("No")
	

