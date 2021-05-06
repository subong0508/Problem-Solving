def pop(board, move):
    cnt = 0
    n = len(board)
    j = move-1
    for i in range(n):
        if board[i][j] != 0:
            stack.append(board[i][j])
            board[i][j] = 0
            break
            
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()
        cnt += 2
    return cnt
    
def solution(board, moves):
    global stack
    stack = []
    answer = 0
    for move in moves:
        answer += pop(board, move)
    return answer