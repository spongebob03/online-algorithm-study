from queue import PriorityQueue

def solution(n, road, k):
    queue = PriorityQueue()
    queue.put([1, 0])
    costs = [float('inf')] * (n+1)
    costs[1] = 0

    while not queue.empty():
        current, current_cost = queue.get()

        for source, destination, cost in road:
            next_cost = cost + current_cost

            # 양방향 도로 (출발지 -> 도착지)
            if source == current and next_cost < costs[destination]:
                costs[destination] = next_cost
                queue.put([destination, next_cost])

            # 양방향 도로 (도착지 -> 출발지)
            if destination == current and next_cost < costs[source]:
                costs[source] = next_cost
                queue.put([source, next_cost])

    return len([c for c in costs[1:] if c <= k])