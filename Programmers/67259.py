from collections import deque

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
INF = int(1e10)

def bfs(x, y, board):
    n = len(board)
    distance = [[INF] * n for _ in range(n)]
    distance[x][y] = 0
    q = deque([(0, x, y, 0, 0)])
    while q:
        cost, x, y, dx, dy = q.popleft()
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                tmp = cost
                if dx == dy == 0:
                    tmp += 100
                elif abs(dxs[i]) == abs(dx):
                    tmp += 100
                else:
                    tmp += 600
                if tmp <= distance[nx][ny]:
                    distance[nx][ny] = tmp
                    q.append((tmp, nx, ny, dxs[i], dys[i]))
    return distance
                
def solution(board):
    answer = 0
    n = len(board)
    answer = bfs(0, 0, board)[n-1][n-1]
    return answer