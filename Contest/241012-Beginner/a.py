def get_inputs():
    N = int(input())
    S = input()
    return N, S

def solve():
    N, S = get_inputs()
    count = 0
    for i in range(N-2):
        if S[i] == "#" and S[i+1] == "." and S[i+2] == "#":
            count += 1
    print(count)
solve()
