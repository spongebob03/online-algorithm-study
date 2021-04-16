def solution(n, s):
    # 최고의 집합이 존재하지 않는 경우 
    # 합이 s인 n개의 자연수가 존재할 수 없는 경우 
    if n > s:
        return [-1]
    
    # 원소들끼리 값이 유사해야 곱이 최대가 됨 
    # s를 n으로 나눈 몫과 나머지  
    share, res = s // n, s % n
    
    # n개의 몫으로 이루어진 result 
    result = [share] * n 
    
    # 합을 s로 만들어주기 위해 나머지를 각 원소에 배분해줌 
    # 오름차순으로 정렬하기 위해 -i 
    for i in range(1,res+1):
        result[-i] += 1
    
    return result