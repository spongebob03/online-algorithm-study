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

    active = 0
    LEFT, RIGHT = 0, 1 
    
    for number in numbers:
        # 1, 4, 7 
        if number in [1,4,7]:
            active = LEFT 

        # 3, 6, 9
        elif number in [3,6,9]:
            active = RIGHT

        # 2, 5, 8, 0 
        else:
            # 왼손이 더 가까이 있으면 왼손이 
            if distance(number, left) < distance(number, right):
                active = LEFT 

            # 오른손이 더 가까이 있으면 오른손이 
            elif distance(number, left) > distance(number, right):
                active = RIGHT

            # 거리가 같으면 왼손잡이냐, 오른손잡이냐에 따라 결정 
            else:
                if hand == 'right':
                    active = RIGHT
                else:
                    active = LEFT 

        if active == LEFT:
            answer += 'L'
            left = number
        else:
            answer += 'R'
            right = number 

    return answer