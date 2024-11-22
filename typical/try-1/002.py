def getInputs():
	N = int(input())
	return N

def isOKP(parenthese):
	score = 0
	for p in parenthese:
		if p == "(":
			score += 1
		else:
			score -= 1
		if score < 0:
			return False
	return score == 0
		

N = getInputs()
parentheses = []
def dfs(i, p, curr):
	curr += p
	if i == N:
		parentheses.append(curr)
		return
	else:
		dfs(i+1, "(", curr)
		dfs(i+1, ")", curr)
dfs(1, "(", "")

for par in parentheses:
	if isOKP(par):
		print(par)

		