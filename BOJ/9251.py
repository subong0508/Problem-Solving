str1 = input()
str2 = input()

n = len(str1)
m = len(str2)
board = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            board[i][j] = board[i-1][j-1] + 1
        else:
            board[i][j] = max(board[i-1][j], board[i][j-1], board[i-1][j-1])

print(board[n][m])