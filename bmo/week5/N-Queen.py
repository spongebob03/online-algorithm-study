def dfs(board, row, n):
    count = 0

    if row == n:
        return 1
    
    for col in range(n):

        for i in range(row):
            if board[i] == col: 
                break
            if board[i] + i == row + col or board[i] - i == col - row:
                break
        else:
            board[row] = col
            count += dfs(board, row+1, n)
            
    return count

def solution(n):
    return dfs([-1]*n, 0, n)