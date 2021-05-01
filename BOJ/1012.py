from collections import deque


t = int(input())

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))

res = []
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                answer += 1
                bfs(i, j)
    res.append(answer)

print(*res, sep='\n')