from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append([int(x) for x in input()])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    if not board[x][y]:
        return 0
    answer = 0
    q = deque([(x, y)])
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        answer += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
                board[nx][ny] = 0
                q.append((nx, ny))
    return answer

res = []
for i in range(n):
    for j in range(n):
        tmp = bfs(i, j, board)
        if tmp != 0:
            res.append(tmp)

res.sort()
print(len(res), *res, sep='\n')