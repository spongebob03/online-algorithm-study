import itertools

def solution(orders, course):
    answer = []
    courses = [dict() for _ in range(len(course))]
    
    for order in orders:
        for i in range(len(course)):
            if course[i] <= len(order):
                for combi in itertools.combinations(order, course[i]):
                    menu = ''.join(sorted(combi))
                    courses[i][menu] = courses[i].get(menu, 0) + 1
    
    for newMenu in courses:
        if not newMenu:
            continue
        max_count = max(newMenu.values())
        if max_count < 2:
            continue
        for key, value in newMenu.items():
            if value == max_count:
                answer.append(key)
    
    return sorted(answer)