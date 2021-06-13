from collections import deque

n, m = list(map(int, input().split()))
pos = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])
answer = 0

for p in pos:
    if queue[0] == p:
        queue.popleft()
    else:
        if queue[len(queue)//2] <= p:
            while queue[0] != p:
                x = queue.pop()
                queue.appendleft(x)
                answer += 1
        else:
            while queue[0] != p:
                x = queue.popleft()
                queue.append(x)
                answer += 1

print('answer:', answer)