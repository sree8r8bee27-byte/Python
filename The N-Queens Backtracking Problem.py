def solveNQueens(n):
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def backtrack(r, cols, posDiag, negDiag):
        if r == n:
            res.append([''.join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                continue
            cols.add(c); posDiag.add(r+c); negDiag.add(r-c)
            board[r][c] = 'Q'
            backtrack(r+1, cols, posDiag, negDiag)
            # Cleanup for next iteration
            cols.remove(c); posDiag.remove(r+c); negDiag.remove(r-c)
            board[r][c] = '.'
            
    backtrack(0, set(), set(), set())
    return res
