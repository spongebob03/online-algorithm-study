from collections import deque 

# 주어진 n*n 행렬을 회전하는 class 
class rotation:
    def __init__(self, x):
        self.x = x
        self.n = len(x)
    
    # self.x를 오른쪽으로 90도 회전 
    def right90(self):
        result = []
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                temp.append(self.x[j][i])
            result.append(temp[::-1])
        self.x = result

    # num만큼 오른쪽으로 90도 회전 
    def rotate(self, num):
        for i in range(num):
            self.right90()
        return self.x


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
# ex. [(0,2), (1,1), (2,1)]을 입력으로 받으면, [(1,-1), (1,0)]을 반환 
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
    
    # 0인 부분들 사이의 차(관계) 
    # ex. lock의 (1,2)와 (2,1)이 0이라면 lock_relations=[(1,-1)]
    lock_relations = check_relation(lock0.copy())

    # key는 4가지 회전 가능 
    for i in range(4):

        # 회전 후 key에서 1인 부분의 index
        key1 = check_idx(r.rotate(i), 1)
        
        possible_keys = []
    
        # 열쇠 모양 확인 
        for k in key1:
            # lock과 모양이 맞는 key의 위치들 
            shape_matching_keys = [k]
            cur_key = k
            for l in lock_relations:
                cur_key = tuple([sum(x) for x in zip(cur_key, l)])
                if cur_key in key1:
                    shape_matching_keys.append(cur_key)
            # 자물쇠의 모든 홈을 빈틈없이 채운 경우 
            if len(shape_matching_keys) == len(lock0):
                possible_keys.append(shape_matching_keys)
                
        
        # 열쇠 모양은 통과
        # 돌기끼리 안 부딪히는지 확인 
        for possible_key in possible_keys:
            
            # key가 1인 부분 중 자물쇠 홈에 대응하지 않는 나머지들 
            residual = [k for k in key1 if k not in possible_key]
            

            # 대응관계: key의 위치가 lock의 위치 어디에 해당하는지 
            # ex. key의 (0,1)이 lock의 (1,0)에 대응한다면 key2lock은 (1-0, 0-1) = (1,-1)
            # 그러면 key의 (2,0)은 lock의 (2,0) + (1,-1) = (3,-1)에 위치할 것을 알 수 있음 
            x,y = possible_key[0]
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