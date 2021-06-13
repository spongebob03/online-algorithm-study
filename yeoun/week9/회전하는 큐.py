from collections import deque 
import sys

class RotatingQueue:
    def __init__(self, N):
        self.queue = deque(range(1, N+1))
        
    # 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
    def computation1(self):
        self.queue.popleft()
    
    # 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
    def computation2(self):
        first = self.queue.popleft()
        self.queue.append(first)
        
    # 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
    def computation3(self):
        last = self.queue.pop()
        self.queue.appendleft(last)

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
N = inputs[0]
M = inputs[1]
targets = inputs[2:]
        
rq = RotatingQueue(N)

count = 0

for target in targets:
    # 뽑아야 하는 숫자가 맨 앞에 있는 경우 
    if target == rq.queue[0]:
        # 연산1 수행 
        rq.computation1()
    
    # 뽑아야 하는 숫자가 앞쪽에 있는 경우 
    # 맨 앞에 올 때까지 연산2 수행, 수행한 만큼 count 증가 
    elif rq.queue.index(target) < len(rq.queue)//2 + 1:
        while target != rq.queue[0]:
            rq.computation2()
            count += 1 
        # 맨 앞에 오면 연산1 수행 
        rq.computation1()
        
    # 뽑아야 하는 숫자가 뒷쪽에 있는 경우
    # 맨 앞에 올 때까지 연산3 수행, 수행한 만큼 count 증가 
    else:
        while target != rq.queue[0]:
            rq.computation3()
            count += 1   
        # 맨 앞에 오면 연산1 수행 
        rq.computation1()

print(count)