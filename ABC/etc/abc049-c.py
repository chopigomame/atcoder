def getInputs():
	S = input()
	return S

components = ["dream", "dreamer", "erase", "eraser"]

def recSearcher(T):
	if T == S:
		return True
	for component in components:
		newT = T + component
		if newT == S[:len(newT)]:
			if recSearcher(newT):
				return True
	return False

S = getInputs()
if recSearcher(""):
	print("YES")
else:
	print("NO")
