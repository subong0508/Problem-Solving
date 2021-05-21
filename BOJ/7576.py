from collections import deque

m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board):
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i, j, cnt))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny, cnt+1))
    return cnt

answer = bfs(board)

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer = -1

print(answer)