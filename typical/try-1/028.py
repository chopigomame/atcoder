import numpy as np
def solve():
    N = int(input())
    MAX = 1002
    summs = [[0 for _ in range(MAX)] for _ in range(MAX)]
    for n in range(N):
        lx, ly, rx, ry = map(int, input().split())
        summs[ly][lx] += 1 #左上
        summs[ry][rx] += 1 #右下
        summs[ly][rx] -= 1 #右上
        summs[ry][lx] -= 1 #左下
    
    accums = [[0]*MAX for _ in range(MAX)]
    for y in range(MAX):
        accum = 0
        for x in range(MAX):
            accum += summs[y][x]
            accums[y][x] = accum
    
    ret = [0 for _ in range(N+1)]
    for x in range(MAX):
        accum = 0
        for y in range(MAX):
            accum += accums[y][x]
            accums[y][x] = accum
            ret[accum] += 1
    print(*ret[1:], sep="\n")

solve()