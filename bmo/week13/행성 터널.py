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
    f = open('bmo/week13/input4.txt', 'r')
    n = int(f.readline())
    parent = [i for i in range(n)]
    nodes = []
    edges = []
    result = 0

    for _ in range(n):
        x, y, z = map(int, f.readline().split())
        nodes.append((_, x, y, z))
    
    # x축 
    nodes.sort(key=lambda x: x[1])
    for i in range(n-1):
        edges.append((nodes[i+1][1] - nodes[i][1], nodes[i][0], nodes[i+1][0]))
    
    # y축
    nodes.sort(key=lambda x: x[2])
    for i in range(n-1):
        edges.append((nodes[i+1][2] - nodes[i][2], nodes[i][0], nodes[i+1][0]))
    
    # z축
    nodes.sort(key=lambda x: x[3])
    for i in range(n-1):
        edges.append((nodes[i+1][3] - nodes[i][3], nodes[i][0], nodes[i+1][0]))
    
    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    print(result)