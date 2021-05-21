def operate(q, operation):
    # 삽입 
    if operation.startswith('I'):
        num = int(operation.split()[-1])
        q += [num]
    # 최댓값 삭제
    elif operation == 'D 1':
        if q:
            q.remove(max(q))
    
    # 최솟값 삭제
    else:
        if q:
            q.remove(min(q))
    
    return q

def solution(operations):
    q = []
    for operation in operations:
        q = operate(q, operation)
    
    # 큐가 비어있는 경우 
    if not q:
        return [0,0]
    
    return [max(q), min(q)]