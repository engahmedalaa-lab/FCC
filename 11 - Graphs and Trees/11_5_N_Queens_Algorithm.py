def dfs_n_queens(n):
    result = []

    if n < 1:
        return result
   
    stack= [([],0)]
    while stack:
        board, row = stack.pop()
        if row == n:
            result.append(board)
            continue
        for col in range(n-1,-1,-1):
            valid_move = True
            for prev_row  in range(row):
                prev_col = board[prev_row]
               
                if prev_col == col:
                    valid_move = False
                    break
               
                if abs(prev_row - row) == abs(prev_col - col):
                    valid_move = False
                    break
           
            if valid_move:
                stack.append((board + [col], row + 1))
    return result

print(dfs_n_queens(4))