t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = []
for _ in range(t):
    n = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))
    
    for j in range(1, n):
        for i in range(2):
            board[i][j] = max(board[i][j] + board[abs(i-1)][j-1], board[i][j-1])

    res.append(max(board[0][-1], board[1][-1]))

print(*res, sep='\n')