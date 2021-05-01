n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        min_value = int(1e9)
        for k in range(3):
            if j == k:
                continue
            if board[i-1][k] < min_value:
                min_value = board[i-1][k]
        board[i][j] += min_value

print(min(board[-1]))