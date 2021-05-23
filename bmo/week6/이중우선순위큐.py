from collections import deque

def solution(operations):
    queue = deque()
    for operation in operations:
        op = operation.split()

        if op[0] == 'I':
            queue.append(int(op[1]))
        else:
            if not queue:
                continue

            queue = deque(sorted(list(queue)))
            if op[1] == '1':
                queue.pop()
            else:
                queue.popleft()

    return [max(queue), min(queue)] if queue else [0, 0]