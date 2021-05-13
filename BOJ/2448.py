n = int(input())

arr = [[' '] * (2*n) for _ in range(n)]

def star(n, x, y):
    if n == 3:
        arr[x][y] = '*'
        arr[x+1][y-1] = arr[x+1][y+1] = '*'
        for i in range(5):
            arr[x+2][y-i+2] = '*'
    else:
        star(n//2, x, y)
        star(n//2, x+n//2, y-n//2)
        star(n//2, x+n//2, y+n//2)

star(n, 0, n-1)

for row in arr:
    print(''.join(row))