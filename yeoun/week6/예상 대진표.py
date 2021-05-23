# a,b 참가자가 현재 라운드에서 만나면 True, 아니면 False 
# 둘의 차가 1이고, 큰 값이 짝수여야 만남 
def check_if_meet(a,b):
    if abs(a-b) == 1 and max(a,b) % 2 == 0:
        return True
    
    return False 

# 다음 라운드에 배정되는 번호를 반환함
def next_num(player):
    # 짝수면 현재 번호를 2로 나눈 값
    if player % 2 == 0:
        return player // 2 
    # 홀수면 (현재 번호 + 1)을 2로 나눈 값 
    else:
        return (player+1)//2 

def solution(n,a,b):
    # a,b가 만나는 라운드의 번호 
    answer = 1
    
    # 현재 라운드에서 만나면 while문 탈출 
    while not check_if_meet(a,b):
        # 다음 라운드의 번호로 갱신 
        a = next_num(a)
        b = next_num(b)
        # 라운드 번호 +1 
        answer += 1 
            
    return answer 

