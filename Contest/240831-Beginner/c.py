import math

def get_inputs():
    N = int(input())
    As = list(map(int, input().split()))
    return N, As

def count_pairs(N):
    count = math.comb(N, 2)
    return count

def solve():
    N, As = get_inputs()
    if N == 1:
        print(1)
        return
    count = 0
    subAs = [As[0], As[1]]
    diff = subAs[1] - subAs[0]
    for i, a in enumerate(As[2:]):
        if a - subAs[-1]  == diff:
            subAs.append(a)
        else:
            count += math.comb(len(subAs), 2)
            subAs = [subAs[-1], a]
            diff = subAs[1] - subAs[0]
    count += math.comb(len(subAs), 2)
    count += N

    print(count)
    
solve()

# なんかダルイ実装になっている。。。他の人どう実装してるんだろ。。。