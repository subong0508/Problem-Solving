n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

zero_cnt = 0
one_cnt = 0

def cut(x, y, n, board):
    global zero_cnt, one_cnt
    if n == 1:
        if board[x][y] == 0:
            zero_cnt += 1
        else:
            one_cnt += 1
    else:
        prev = board[x][y]
        same = True
        for i in range(n):
            for j in range(n):
                if board[x+i][y+j] != prev:
                    same = False
        if same:
            if prev == 0:
                zero_cnt += 1
            else:
                one_cnt += 1
        else:
            next_n = n // 2
            for i in range(2):
                for j in range(2):
                    cut(x + i * next_n, y + j * next_n, next_n, board)

cut(0, 0, n, board)

print(zero_cnt, one_cnt, sep='\n')