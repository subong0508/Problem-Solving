from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    q = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    board[x][y] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1 and not visited[nx][ny]:
                board[nx][ny] = 2
                visited[nx][ny] = True
                q.append((nx, ny))

def melt(board):
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                q.append((i, j))
    dq = deque()
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 2:
                cnt += 1
        if cnt >= 2:
            dq.append((x, y))
    answer = len(dq)
    while dq:
        x, y = dq.popleft()
        board[x][y] = 2
    return answer

answer = 0
while True:
    bfs(0, 0, board)
    if not melt(board):
        break
    answer += 1

print(answer)