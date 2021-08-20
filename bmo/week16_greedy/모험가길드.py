n = 5
fears = [4, 3, 1, 1, 2]
fears.sort()
cnt = 0
stack = []

for fear in fears:
    stack.append(fear)
    if max(stack) == len(stack):
        cnt += 1
        stack = []

print(cnt)