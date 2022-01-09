n, m = map(int, input().split())

idx_name = {}
name_idx = {}

for i in range(1, n+1):
    name = input()
    idx_name[i] = name
    name_idx[name] = i

for _ in range(m):
    q = input()
    if q.isdigit():
        print(idx_name[int(q)])
    else:
        print(name_idx[q])