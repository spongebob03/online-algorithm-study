"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # queue with nodes
        queue = deque([root])
        # queue with depths
        depth = deque([1])
        
        while queue:
            node = queue.popleft()
            d = depth.popleft()
            
            # check if depth is same 
            if depth and depth[0] == d:
                node.next = queue[0]
            
            # prevent error when node in None 
            if node:
                children = [node.left, node.right]
                for child in children:
                    if child:
                        queue.append(child)
                        # increase depth by 1 
                        depth.append(d+1)
            
        return root