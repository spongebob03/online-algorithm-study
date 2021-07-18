import heapq

def solution(jobs):
    answer, time, idx = 0, 0, 0
    start = -1
    heap = []

    while idx < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = time
            time += current[0]
            answer += time - current[1]
            idx += 1
        else:
            time += 1
            
    return int(answer / len(jobs))

if __name__ == '__main__':
    print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))