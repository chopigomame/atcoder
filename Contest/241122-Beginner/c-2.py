def solve():
    N = int(input())
    if N == 0:
        print(0)
        return

    S = input() + " "

    nums = [0, 0]
    searching = 1
    max_num = 0

    for i, s in enumerate(S):
        if s == str(searching):
            nums[searching - 1] += 1

        elif searching == 1 and s == "/":
        # elif  s == "/":
            searching = 2

        else:
            max_num = max(min(nums) * 2 + 1, max_num)
            searching = 1

            nums = [0, 0]
            if s == "1":
                nums[0] += 1
    
    print(max_num)

solve()