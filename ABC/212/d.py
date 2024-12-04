import heapq

def solve():
    Q = int(input())
    accum = 0
    balls = []
    for _ in range(Q):
        query = input()
        qtype = query[0]

        if qtype == "1":
            x = int(query.split()[1])
            x -= accum
            heapq.heappush(balls, x)
        elif qtype == "2":
            x = int(query.split()[1])
            accum += x
        else:
            ball = heapq.heappop(balls)
            print(ball + accum)

solve()