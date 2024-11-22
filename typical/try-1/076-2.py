def get_inputs():
    N = int(input())
    As = list(map(int, input().split()))
    return N, As

def solve():
    N, As = get_inputs()
    sumAs = sum(As)

    DPs = [{} for i in range(N+1)]
    DPs[0][0] = True
    # 1回目
    for i, A in enumerate(As, 1):
        DPs[i][A] = True
        for key in DPs[i-1].keys():
            DPs[i][key+A] = True
    # 2回目
    for i, A in enumerate(As, 1):
        if i==1:
            i_prev = N
        else:
            i_prev = i-1
        for key in DPs[i_prev].keys():
            new_key = key + A
            if new_key < sumAs:
                DPs[i][new_key] = True

    tenth = sumAs//10
    res = "No"
    for i in range(1, N+1):
        if tenth in DPs[i].keys():
            res = "Yes"
    print(res)


solve()