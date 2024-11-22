def solve():
    N = int(input())
    S = input()

    if N % 2 == 0:
        print("No")
        return

    len_1 = (N+1)//2 - 1
    for i in range(len_1):
        if S[i] != "1":
            print("No")
            return
    
    if S[len_1] != "/":
        print("No")
        return

    for i in range(len_1+1, N):
        if S[i] != "2":
            print("No")
            return
    
    print("Yes")
    return

solve()
            
