import math
def solve():
    cost = 0
    N = int(input())
    prevX, prevY = 0, 0
    for n in range(N):
        currX, currY = map(int, input().split())
        cost += math.sqrt((prevX - currX)**2 + (prevY - currY)**2)
        prevX, prevY = currX, currY
    currX, currY = 0, 0
    cost += math.sqrt((prevX - currX)**2 + (prevY - currY)**2)
    print(cost)


solve()