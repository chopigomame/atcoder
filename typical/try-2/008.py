def get_inputs():
    N = int(input())
    S = input()
    return N, S

def solve():
    N, S = get_inputs()
    DP = {"":1, "a":0, "at":0, "atc":0, "atco":0, "atcod":0, "atcode":0, "atcoder":0}
    dp_map = {"a":"" , "t":"a", "c": "at", "o": "atc", "d": "atco", "e":"atcod", "r":"atcode"}

    for s in S:
        if s in dp_map:
            base = dp_map[s]
            DP[base+s] += DP[base]
    print(DP["atcoder"] % (10**9 + 7))
    
solve()