def printTree(tree):
    s = ''
    todo = [(1, True)]
    while todo:
        i, pl = todo.pop()
        a, b = tree[i]
        if pl:
            todo.append((i, False))
            if a != -1:
                todo.append((a, True))
        else:
            s += ' %d' % i
            if b != -1:
                todo.append((b, True))
    print(s[1:])


def swapNodes(tree, k):
    todo = [(1, 1)]
    while todo:
        i, d = todo.pop()
        a, b = tree[i]
        if d % k == 0:
            tree[i] = b, a
        if a != -1:
            todo.append((a, d + 1))
        if b != -1:
            todo.append((b, d + 1))


n = int(input())
nodes = [None]
for _ in range(n):
    a, b = map(int, input().split())
    nodes.append((a, b))

t = int(input())
for _ in range(t):
    k = int(input())
    swapNodes(nodes, k)
    printTree(nodes)
