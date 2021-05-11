import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = []
for _ in range(n):
    board.append(input().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

def bfs(x, y, board, visited):
    q = deque([(x, y, 0, 1)])
    while q:
        x, y, broken, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == '0' and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    q.append((nx, ny, broken, cnt+1))
                elif board[nx][ny] == '1' and not broken and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, 1, cnt+1))
    return -1

print(bfs(0, 0, board, visited))