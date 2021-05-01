n = int(input())
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

# number of -1s, 0s, 1s
cnts = [0, 0, 0]

def cut(x, y, n, board):
    same = True
    prev = board[x][y]
    for i in range(n):
        for j in range(n):
            if board[x+i][y+j] != prev:
                same = False
                break
    if same:
        if prev == -1:
            cnts[0] += 1
        elif prev == 0:
            cnts[1] += 1
        else:
            cnts[2] += 1
    elif n >= 3:
        next_n = n // 3
        for i in range(3):
            for j in range(3):
                cut(x + i * next_n, y + j * next_n, next_n, board)

cut(0, 0, n, board)

print(*cnts, sep='\n')