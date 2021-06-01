# 키보드를 2d array로 보고 [행,열]을 반환하도록 함 
def get_index(number):
    if number not in [3,6,9, '#', '*', 0]:
        pos = [number//3, number%3-1]
    elif number in [3,6,9]:
        pos = [number//3-1, 2]
    else:
        if number == '*':
            pos = [3,0]
        elif number == 0:
            pos = [3,1]
        else:
            pos = [3,2]
    return pos

# 키보드를 2d array로 보고, 해당하는 index의 차를 구해 거리를 구함 
def distance(number, current_pos):
    distance = 0
    for x, y in zip(get_index(number), get_index(current_pos)):
        distance += abs(x-y)
    return distance
    

def solution(numbers, hand):
    answer = ''
    # 현재 왼손, 오른손의 위치 
    left = '*'
    right = '#'
    
    # 왼손, 오른손의 담당 번호들 
    lefts = [1,4,7]
    rights = [3,6,9]
    
    for number in numbers:
        # 1, 4, 7 
        if number in lefts:
            answer += 'L'
            left = number
        # 3, 6, 9
        elif number in rights:
            answer += 'R'
            right = number
        # 2, 5, 8, 0 
        else:
            # 왼손이 더 가까이 있으면 왼손이 
            if distance(number, left) < distance(number, right):
                answer += 'L'
                left = number 
            # 오른손이 더 가까이 있으면 오른손이 
            elif distance(number, left) > distance(number, right):
                answer += 'R'
                right = number 
            # 거리가 같으면 왼손잡이냐, 오른손잡이냐에 따라 결정 
            else:
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number
    
    return answer