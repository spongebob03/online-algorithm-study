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
    f = open('bmo/week13/input1.txt', 'r')
    n, m = map(int, f.readline().split())
    parent = [i for i in range(n+1)]

    for i in range(n):
        cities = list(map(int, f.readline().split()))
        for j in range(n):
            if cities[j] == 1:
                union_parent(parent, i+1, j+1)

    path = set()
    for city in map(int, f.readline().split()):
        path.add(parent[city])
    
    print('NO') if len(path) > 1 else print('YES')