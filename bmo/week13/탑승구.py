def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    f = open('bmo/week13/input2.txt', 'r')
    g = int(f.readline())
    p = int(f.readline())
    parent = [i for i in range(g+1)]
    result = 0

    for _ in range(p):
        gate = int(f.readline())
        a = find_parent(parent, gate)
        if a == 0:
            break
        union_parent(parent, a, a-1)
        result += 1
    print(result)