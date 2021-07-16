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
    f = open('bmo/week13/input3.txt', 'r')
    n, m = map(int, f.readline().split())
    parent = [i for i in range(n+1)]
    edges = []
    result = 0

    for _ in range(m):
        a, b, cost = map(int, f.readline().split())
        edges.append((a, b, cost))

    edges.sort(key=lambda x: x[2])
    total = 0

    for edge in edges:
        a, b, cost = edge
        total += cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    print(total - result)