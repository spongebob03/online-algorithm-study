import math 
from collections import Counter

# 소수 판별하기 
def isPrime(num):
    if num == 1:
        return False 
    
    if num == 2:
        return True 
    
    # 에라스토로스의 체
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True 

# 소인수분해하기 
# ex. 4 -> [2,2]
# ex. 14 -> [2,7]
def factorize(num, result):
    result = []
    
    # 그 자체로 소수거나 1이라면 자기 자신만 반환 
    if isPrime(num) or num == 1:
        return [num]
    
    for i in range(2, (num//2)+1):
        if num % i == 0 and isPrime(i):
            count = 1
            share = num // i 
            # 제곱수를 처리하기 위한 while문 
            while share != 1:
                if share % i != 0:
                    break
                share = share // i 
                count += 1 
            result += [i] * count 
    
    return result

# N개의 최소공배수 구하기 
def solution(arr):
    answer = 1 
    # 주어진 숫자를 소인수분해한 결과의 중복을 포함한 합집합 
    result = Counter()
    
    for num in arr:
        result |= Counter(factorize(num,[]))
    
    # 소인수분해한 결과의 합집합을 곱해 최종 답을 계산
    for key in result:
        answer *= key ** result[key]
        
    return answer