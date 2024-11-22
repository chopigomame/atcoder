def solve():
    S = input()
    N = len(S)

    if N % 2 != 0:
        print("No")
        return

    len_1 = N//2
    counter = {}
    for i in range(len_1):
        if S[2*i + 1] != S[2*i]:
            print("No")
            return

        s = S[2*i + 1]
        counter.setdefault(s, 0)
        counter[s] += 2
        if counter[s] != 2:
            print("No")
            return
    
    print("Yes")
    return

solve()
            

