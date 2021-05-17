from collections import defaultdict

def solution(routes):
    road = defaultdict(lambda:[])
    all_cars = list(range(len(routes)))
    
    # road[위치] = [자동차 index]
    for i, route in enumerate(routes):
        enter, exit = route
        road[enter].append(i)
        road[exit].append(i)
    
    on_road = []
    hist = []
    # 각 위치에 따라 포착할 수 있는 자동차들의 리스트 
    for pos in sorted(list(set(road.keys()))):
        on_road += road[pos]
        current_cars = list(set(on_road))
        if current_cars not in hist:
            hist.append(current_cars)
        
        for car in road[pos]:
            # 두 번째 등장한 건 도로에서 나간다는 의미 
            if on_road.count(car) == 2:
                on_road = [r for r in on_road if r != car]
    
    answer = 1

    # 가장 길이가 긴, 즉 가장 많은 자동차를 찍을 수 있는 곳에 첫번째 카메라 놓기 
    first_cam = max(hist, key=len)
    hist.remove(first_cam)
    # 아직 찍지 못한 자동차들 
    residual = set(all_cars) - set(first_cam)
    
    # 못 찍은 자동차가 있는 한 반복 
    while residual:
        max_count = 0 
        for h in hist:
            count = 0 
            for r in residual:
                count += h.count(r)
            if count > max_count:
                max_count = count
                max_cam = h
                # 모든 자동차를 찍었으면 loop 탈출 
                if count == len(residual):
                    break
        
        hist.remove(max_cam)
        residual -= set(max_cam)
        answer += 1
    
    return answer