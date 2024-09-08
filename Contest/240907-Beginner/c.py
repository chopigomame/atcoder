def get_inputs():
    S = input()
    T = input()
    return S, T

def solve():
    S, T = get_inputs()
    down_diffs = []
    up_diffs = []
    for i, (s, t) in enumerate(zip(S, T)):
        ord_s, ord_t = ord(s),  ord(t)
        if ord_s > ord_t:
            down_diffs.append([i, t])
        elif ord_s < ord_t:
            up_diffs.append([i, t])
            
    X = []
    S_list = list(S)
    for i, d in down_diffs:
        S_list[i] = d
        X.append("".join(S_list))
    
    for i, d in up_diffs[::-1]:
        S_list[i] = d
        X.append("".join(S_list))
        
    print(len(X))
    for x in X:
        print(x)

solve()