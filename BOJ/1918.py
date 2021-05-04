eq = input()

stack = []
answer = ''
for x in eq:
    if x == '(':
        stack.append(x)
    elif x == '+' or x == '-':
        while stack and stack[-1] in ('+', '-', '*', '/'):
            answer += stack.pop()
        stack.append(x)
    elif x == '*' or x == '/':
        while stack and stack[-1] in ('*', '/'):
            answer += stack.pop()
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    else:
        answer += x

while stack:
    answer += stack.pop()

print(answer)