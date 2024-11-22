def solve():
    N = input()
    ok1 = N.count("1") == 1
    ok2 = N.count("2") == 2
    ok3 = N.count("3") == 3
    return ok1 * ok2 * ok3

if solve():
    print("Yes")
else:
    print("No")
