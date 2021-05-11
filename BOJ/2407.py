n, m = map(int, input().split())

a = 1
b = 1
for _ in range(m):
    a *= n
    b *= m
    n -= 1
    m -=1 

print(a // b)