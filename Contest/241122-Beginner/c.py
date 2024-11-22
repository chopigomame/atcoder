def solve():
    N = int(input())
    S = input() + " "

    num_1 = 0
    num_2 = 0
    counting_1 = True
    counting_2 = False
    max_num = 0

    for i, s in enumerate(S):
        if counting_1 and S[i] == "1":
            num_1 += 1
            
        elif counting_1 and S[i] == "/":
            counting_1 = False
            counting_2 = True

        elif counting_2 and S[i] == "2" and num_2 + 1 <= num_1:
            num_2 += 1
        
        else:
            max_num = max(min(num_1, num_2) * 2 + 1, max_num)

            counting_1 = True
            counting_2 = False
            num_1 = 0
            num_2 = 0
    
    print(max_num)

solve()
            

