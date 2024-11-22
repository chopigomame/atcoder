from collections import deque

def get_inputs():
	H, W = map(int, input().split())
	Q = int(input())
	return H, W, Q

def get_query():
	inp = input()
	if inp[0] == "1":
		t, r, c = map(int, inp.split(" "))
		return t, r-1, c-1
	elif inp[0] == "2":
		t, ra, ca, rb, cb  = map(int, inp.split(" "))
		return t, ra-1, ca-1, rb-1, cb-1
	
def solve():
	H, W, Q = get_inputs()
	cells = [[0] * W for _ in range(H)]
	for q in range(Q):
		query = get_query()
		if query[0] == 1:
			cells[query[1]][query[2]] = 1
		else:
			ra, ca, rb, cb = query[1:]
			output = "No"
			accessed_cells = [[0] * W for _ in range(H)]
			if cells[ra][ca] == 1 and cells[ra][ca] == 1:
				s = deque([[ra, ca]])
				while s:
					r, c = s.pop()
					if r == rb and c == cb:
						output = "Yes"
						break
					accessed_cells[r][c] = 1
					for dx, dy in ([-1, 0], [0, 1], [1, 0], [0, -1]):
						nr, nc = r + dx, c + dy
						if 0 <= nr < H and 0 <= nc < W and accessed_cells[nr][nc] != 1 and cells[nr][nc] == 1:
							s.append([nr, nc])
			print(output)
			
solve()
					
