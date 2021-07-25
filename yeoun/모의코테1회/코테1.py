# https://www.acmicpc.net/problem/11724
import sys

inputs = list(map(int, sys.stdin.read().split()))

N = inputs[0]
M = inputs[1]

connected = []
for i in range(0, len(inputs[2:]), 2):
    a, b = inputs[2:][i], inputs[2:][i + 1]
    connected.append((a, b))

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


parent = [i for i in range(N+1)]

for con in connected:
    a, b = con
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

parent_no_dup = list(set(parent[1:]))
ans = len(parent_no_dup)

for i in range(len(parent_no_dup)-1):
    if parent[parent_no_dup[i]] == parent[parent_no_dup[i+1]]:
        ans -= 1

print(ans)