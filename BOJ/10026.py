from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(input())

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_same(x, y, nx, ny, board):
    if (board[x][y] == 'R' and board[nx][ny] == 'G') or (board[x][y] == 'G' and board[nx][ny] == 'R'):
        return True
    return False

def bfs(x, y, board, visited, flag=False):
    if visited[x][y]:
        return False
    visited[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[x][y] == board[nx][ny] or (flag and is_same(x, y, nx, ny, board)):
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return True


a = 0
b = 0
for i in range(n):
    for j in range(n):
        a += bfs(i, j, board, visited1)
        b += bfs(i, j, board, visited2, True)           

print(a, b)