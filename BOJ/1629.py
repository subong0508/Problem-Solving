a, b, c = map(int, input().split())

def pow(a, b):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return pow(a, b//2) ** 2 % c
    else:
        return pow(a, b//2) ** 2 * a % c

print(pow(a, b))