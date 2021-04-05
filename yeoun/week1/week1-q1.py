from collections import deque 

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while trucks:
        current_truck = trucks.popleft()
        
        # 현재 트럭을 다리에 올릴 수 있는 경우 
        if sum(bridge) + current_truck <= weight:
            bridge.popleft() # 한 칸씩 앞으로 당기고
            bridge.append(current_truck) # 현재 트럭을 맨 뒤에 추가 
            answer += 1 

        # 현재 트럭을 다리에 올릴 수 없는 경우
        else:
            bridge_sum = sum(bridge)
            # 현재 트럭을 다리에 올릴 수 있을 때까지 
            while bridge_sum + current_truck > weight:
                popped = bridge.popleft() # 한 칸씩 앞으로 당김 
                bridge.append(0) # (queue의 길이 보존을 위해)
                answer += 1 
                bridge_sum -= popped # while문에서 여러 번 sum을 계산하지 않도록 
            # 현재 트럭을 맨 뒤에 위치시킴     
            bridge[-1] = current_truck
    # while문이 끝나면 마지막 트럭까지 다리 위에 올라온 상태 
    
    # 마지막 트럭이 다리를 끝까지 건너려면 bridge_length만큼의 시간이 소요됨     
    return answer + bridge_length