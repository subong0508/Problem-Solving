from collections import deque

m, n, h = map(int, input().split())
board = []
for i in range(h):
    board.append([])
    for j in range(n):
        board[i].append(list(map(int, input().split())))

dx = [-1, 1,  0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(board):
    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    q.append((i, j, k, cnt))
    while q:
        x, y, z, cnt = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and board[nx][ny][nz] == 0:
                board[nx][ny][nz] = 1
                q.append((nx, ny, nz, cnt+1))
    return cnt

answer = bfs(board)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                answer = -1

print(answer)