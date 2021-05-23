from collections import defaultdict

def solution(participant, completion):
    participants = defaultdict(int)
    
    for name in participant:
        participants[name] += 1
    
    for name in completion:
        participants[name] -= 1
    
    for key, value in participants.items():
        if value == 1:
            return key