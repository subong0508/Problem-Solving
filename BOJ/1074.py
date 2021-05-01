n, r, c = map(int, input().split())
n = 2 ** n

answer = 0

def visit(x, y, n):
    global answer
    # print("x: %d, y: %d, n: %d, answer: %d" % (x, y, n, answer))
    if x == r and y == c:
        return
    elif n >= 2:
        if x <= r < x+n//2 and y <= c < y+n//2:
            visit(x, y, n//2)
        elif x <= r < x+n//2:
            answer += (n // 2) * (n // 2)
            visit(x, y+n//2, n//2)
        elif y <= c < y+n//2:
            answer += 2 * (n // 2) * (n // 2)
            visit(x+n//2, y, n//2)
        else:
            answer += 3 * (n // 2) * (n // 2)
            visit(x+n//2, y+n//2, n//2)

visit(0, 0, n)

print(answer)