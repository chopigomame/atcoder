def get_inputs():
    N = int(input())
    As = []
    for n in range(N):
        As.append(list(input()))
    return N, As

def solve():
    N, As = get_inputs()
    Bs = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N//2):
        state = (i+1) % 4
        for y in range(i, N-i):
            if i < y < N-i-1:
                loop = [i, N-i-1]
            else:
                loop = range(i, N-i)
            for x in loop:
                if state == 0:
                    ty, tx = y, x
                elif state == 1:
                    ty, tx = N-1-x, y
                elif state == 2:
                    ty, tx = N-1-y, N-1-x
                elif state == 3:
                    ty, tx = x, N-1-y
                Bs[y][x] = As[ty][tx]
    for b in Bs:
        print(*b, sep="")

solve()