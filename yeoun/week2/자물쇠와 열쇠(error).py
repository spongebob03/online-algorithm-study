# 오답: 17
from collections import deque 

# 주어진 n*n 행렬을 회전하는 class 
class rotation:
    def __init__(self, x):
        self.x = x
        self.n = len(x)
    
    def right90(self):
        result = []
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                temp.append(self.x[j][i])
            result.append(temp[::-1])
        return result
    
    def right180(self):
        return [row[::-1] for row in self.x][::-1]
    
    def left90(self):
        result = []
        for i in range(self.n-1, -1, -1):
            temp = []
            for j in range(self.n):
                temp.append(self.x[j][i])
            result.append(temp)
        return result
    
    def rotate(self, num):
        # 0을 입력 받으면 x 그대로 반환 
        if num == 0:
            return self.x
        # 1을 입력 받으면 오른쪽으로 90도 회전한 x를 반환 
        elif num == 1:
            return self.right90()
        # 2를 입력 받으면 오른쪽으로 180도 회전한 x를 반환 
        elif num == 2:
            return self.right180()
        # 3을 입력 받으면 왼쪽으로 90도 회전한 x를 반환 
        else: # num == 3
            return self.left90()

# n*n 행렬 중 값이 val인 부분의 index들을 리스트로 반환 
def check_idx(matrix, val):
    result = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == val:
                result.append((i,j))
    return result 

# 좌표들의 리스트들을 입력 받으면, 연속하는 각 좌표들의 차를 반환
def check_relation(q):
    relations = []
    while q:
        cur = q.popleft()
        if q:
            x,y = cur
            a,b = q[0]
            relations.append((a-x, b-y))
    return relations

def solution(key, lock):
    n = len(lock)
    r = rotation(key)
                        
    # lock에서 0인 부분의 index 
    lock0 = deque(check_idx(lock, 0))
    
    # 열쇠를 꽂을 곳이 없음 
    if lock0 == deque():
        return True 
    
    # 0인 부분들 사이의 차 
    # ex. lock의 (1,2)와 (2,1)이 0이라면 lock_relations=[(1,-1)]
    # 그러면 (1,2) + (1,-1) = (2,1) 
    lock_relations = check_relation(lock0.copy())
    
    # key는 4가지 회전 가능 
    for i in range(4):

        # key에서 1인 부분의 index
        key1 = check_idx(r.rotate(i), 1)
            
        # None: 열쇠 모양 달라서 열 수 없음 
        # None이 아닌 경우: 열쇠 모양은 통과, 나머지 부분 안 부딪히는지(돌기끼리 만나지 않는지) 확인 필요 
        start_key = None
    
        # 열쇠 모양 확인 
        for k in key1:
            # lock과 모양이 맞는 key의 위치들 
            real_keys = [k]
            cur_key = k
            for l in lock_relations:
                cur_key = tuple([sum(x) for x in zip(cur_key, l)])
                if cur_key in key1:
                    real_keys.append(cur_key)
            # 자물쇠의 모든 홈을 빈틈없이 채운 경우 
            if len(real_keys) == len(lock0):
                start_key = real_keys[0] # k
                break
        
        
        # 열쇠 모양은 통과
        # 돌기끼리 안 부딪히는지 확인 
        if start_key:
            # key가 1인 부분 중 자물쇠 홈에 대응하지 않는 나머지들 
            residual = [k for k in key1 if k not in real_keys]
            
            # 대응관계: key의 위치가 lock의 위치 어디에 해당하는지 
            # ex. key의 (0,1)이 lock의 (1,0)에 대응한다면 key2lock은 (1-0, 0-1) = (1,-1)
            # 그러면 key의 (2,0)은 lock의 (2,0) + (1,-1) = (3,-1)에 위치할 것을 알 수 있음 
            x,y = start_key
            a,b = lock0[0]
            key2lock = (a-x,b-y)
        
            count = 0
            for res in residual:
                pos = [sum(x) for x in zip(res, key2lock)]
                # 각 residual이 lock에서의 위치가 자물쇠 영역 바깥인 경우
                if (pos[0] not in range(n)) or (pos[1] not in range(n)):
                    count += 1 

            # 부딪힐 부분이 자물쇠 영역 밖에 있어서 상관 없는 경우 True 
            if count == len(residual):
                return True

                        
    return False