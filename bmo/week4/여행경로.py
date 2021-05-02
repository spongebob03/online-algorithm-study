def solution(tickets):
    answer = []
    flight = dict()

    for source, destination in tickets:
        flight[source] = flight.get(source, []) + [destination]
    for source in flight:
        flight[source].sort(reverse=True)
    
    stack = ["ICN"]

    while stack:
        if stack[-1] not in flight.keys() or not flight[stack[-1]]:
            answer.append(stack.pop())
        else:
            stack.append(flight[stack[-1]].pop())
    
    return answer[::-1]