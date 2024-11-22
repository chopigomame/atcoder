def solve():
    N = int(input())
    As = list(map(int, input().split()))
    As.append("a")

    ans = 0
    for s in [0, 1]:
        _As = As[s:]
        counter = {}
        length = len(_As)
        for i in range(length):
            if 2*i >= length:
                ans = max(len(counter.keys()) * 2, ans)
                break
            if _As[2*i] == _As[2*i - 1]:
                A = _As[2*i - 1]
                counter.setdefault(A, 0)
                counter[A] += 2
                if counter[A] != 2:
                    ans = max(len(counter.keys()) * 2, ans)
                    counter = {A:2}
    
    print(ans)

solve()
