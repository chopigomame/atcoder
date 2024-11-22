def solve():
    s_ab, s_ac, s_bc = input().split()
    if s_ab == ">":
        order = ["B", "A"]
        index_a = 1
    else:
        order = ["A", "B"]
        index_a = 0

    if s_ac == ">":
        len_prob = index_a + 1
        if len_prob == 1:
            return "A"
        if s_bc == ">":
            return "B"
        else:
            return "C"
    else:
        len_prob = 2 - index_a
        if len_prob == 1:
            return "A"
        if s_bc == ">":
            return "C"
        else:
            return "B"

print(solve())

# 結局、整理された良い方法が思いつかなかった。。。