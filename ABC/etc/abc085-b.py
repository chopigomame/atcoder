def getInputs():
	N = int(input())
	ds = []
	for _ in range(N):
		ds.append(int(input()))
	return ds

ds = getInputs()

uniqueD = []
for d in ds:
	if not d in uniqueD:
		uniqueD.append(d)
print(len(uniqueD))
	
