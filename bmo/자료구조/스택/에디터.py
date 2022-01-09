from collections import deque

arr = [s for s in input()]
n = len(arr)
cursor = n

m = int(input())
left = deque(arr)
right = deque()

for _ in range(m):
    cmd = input()
    if cmd[0] == 'L' and left:
        right.appendleft(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.popleft())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        c = cmd.split()[1]
        left.append(c)

print(''.join(left), end='')
print(''.join(right))