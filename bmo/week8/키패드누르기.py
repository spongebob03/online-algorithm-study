def distance(next_pos, hand_pos):
    dist = 0
    for i, next_i in zip(next_pos, hand_pos):
        dist += abs(next_i - i)
    return dist

def solution(numbers, hand):
    answer = ""
    active = 0
    LEFT, RIGHT = 0, 1
    l, r = (3, 0), (3, 2)
    pos = {  1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2), 
                7:(2, 0), 8:(2, 1), 9:(2, 2), 0: (3, 1)}
    for number in numbers:
        if number in (1, 4, 7):
            active = LEFT
        elif number in (3, 6, 9):
            active = RIGHT
        else:
            l_dist = distance(pos[number], l)
            r_dist = distance(pos[number], r)
            if l_dist < r_dist:
                active = LEFT
            elif r_dist < l_dist:
                active = RIGHT
            else:
                active = RIGHT if hand == "right" else LEFT
        
        if active == LEFT:
            answer += "L"
            l = pos[number]
        else:
            answer += "R"
            r = pos[number]

    return answer
