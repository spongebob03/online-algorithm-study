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
        nodes.append((x, y, z))
    
    # 뭔가... 이부분 때문에 메모리 초과인거 같은데...
    for i in range(n):
        for j in range(i+1, n):
            edges.append((min([abs(nodes[i][0]-nodes[j][0]), abs(nodes[i][1]-nodes[j][1]), abs(nodes[i][2]-nodes[j][2])]), i, j))

    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    print(result)