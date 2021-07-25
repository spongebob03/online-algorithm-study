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
    f = open('bmo/test01/test1.txt')
    n, m = map(int, f.readline().split())
    parent = [i for i in range(n+1)]
    edges = []

    for _ in range(m):
        a, b = map(int, f.readline().split())
        edges.append((a, b))
        edges.append((b, a)) # 양방향
    
    edges.sort()

    for edge in edges:
        a, b = edge
        union_parent(parent, a, b)
    
    print(parent[1:])
    print(len(set(parent[1:])))