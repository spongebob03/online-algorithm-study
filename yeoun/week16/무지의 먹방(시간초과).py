def solution(food_times, k):
    # 먹는데 가장 오래 걸리는 음식 
    max_time = max(food_times)
    x = []
    # 먹을 수 있는 횟수 만큼 index 반복 
    # list of list를 만들기 위해 각 list의 길이는 max_time으로 통일
    # 더 이상 먹을 수 없는 경우 -1로 채움 
    for i, ft in enumerate(food_times):
        x.append([i] * ft + [-1] * (max_time - ft))
    # transpose 
    y = list(map(list, zip(*x)))
    # -1 제외 
    flat_y = [item for sublist in y for item in sublist if item >= 0]
    
    # k번째 음식의 index + 1 
    # 먹을 수 있는 음식이 없으면 -1
    return flat_y[k] + 1 if len(flat_y) > k else -1