def getGroup(arr):
    group = dict()
    for letter in zip(arr, arr[1:]):
        c = ''.join(letter).upper()
        if c.isalpha():
            group[c] = group.get(c, 0) + 1
    return group

def solution(str1, str2):
    group1 = getGroup(str1)
    group2 = getGroup(str2)
    intersection = 0
    union = 0

    for c in (set(group1.keys()) & set(group2.keys())):
        intersection += min(group1.get(c, 0), group2.get(c, 0))

    for c in (set(group1.keys()) | set(group2.keys())):
        union += max(group1.get(c, 0), group2.get(c, 0))
    
    return int((intersection / union) * 65536) if union != 0 else 65536