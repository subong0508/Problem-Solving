import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(input().rstrip())

stack = []

def quad_tree(x, y, n, board):
    num = board[x][y]
    same = True
    for i in range(n):
        for j in range(n):
            if same and board[x+i][y+j] != num:
                same = False
    if same:
        stack.append(num)
    elif n >= 2:
        stack.append('(')
        next_n = n // 2
        for i in range(2):
            for j in range(2):
                quad_tree(x + i * next_n, y + j * next_n, next_n, board)
        stack.append(')')

quad_tree(0, 0, n, board)

print(''.join(stack))