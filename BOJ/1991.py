n = int(input())
tree = {}
for _ in range(n):
    parent, lchild, rchild = input().split()
    tree[parent] = (lchild, rchild)

def preorder(parent, tree, answer):
    if parent not in tree:
        return ''
    answer += parent
    if tree[parent][0] != '.':
        answer += preorder(tree[parent][0], tree, '')
    if tree[parent][1] != '.':
        answer += preorder(tree[parent][1], tree, '')
    return answer

def inorder(parent, tree, answer):
    if parent not in tree:
        return ''
    if tree[parent][0] != '.':
        answer += inorder(tree[parent][0], tree, '')
    answer += parent
    if tree[parent][1] != '.':
        answer += inorder(tree[parent][1], tree, '')
    return answer

def postorder(parent, tree, answer):
    if parent not in tree:
        return ''
    if tree[parent][0] != '.':
        answer += postorder(tree[parent][0], tree, '')
    if tree[parent][1] != '.':
        answer += postorder(tree[parent][1], tree, '')
    answer += parent
    return answer

funcs = [preorder, inorder, postorder]
for func in funcs:
    print(func('A', tree, ''))