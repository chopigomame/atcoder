def get_inputs():
    H, W, N = map(int, input().split())
    ABs = []
    for _ in range(N):
        A, B = map(int, input().split())
        ABs.append([A, B])
    return H, W, N, ABs

def solve():
    H, W, N, ABs = get_inputs()

    existing_rows = [e[0] for e in sorted(ABs, key=lambda x:x[0])]
    existing_columns = [e[1] for e in sorted(ABs, key=lambda x:x[1])]

    row_substract_num = 0
    row_substract_nums = {}
    curr_row = 1
    for row in existing_rows:
        if row in row_substract_nums.keys():
            continue
        row_substract_num += row - curr_row
        row_substract_nums[row] = row_substract_num
        curr_row = row + 1

    column_substract_num = 0
    column_substract_nums = {}
    curr_column = 1
    for column in existing_columns:
        if column in column_substract_nums.keys():
            continue
        column_substract_num += column - curr_column
        column_substract_nums[column] = column_substract_num
        curr_column = column + 1
        
    for i in range(N):
        A, B = ABs[i]
        print(A - row_substract_nums[A], B - column_substract_nums[B])

solve()