from collections import deque

n, m = map(int, input().split())
board = [[]]
for _ in range(n):
    board.append([0] + list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(1, 1, 1)])
visited = [[False] * (m+1) for _ in range(n+1)]
visited[1][1] = True
while q:
    x, y, cnt = q.popleft()
    if x == n and y == m:
        print(cnt)
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= m and board[nx][ny] == '1' and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))