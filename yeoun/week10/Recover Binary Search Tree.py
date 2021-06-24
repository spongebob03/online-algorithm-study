# BST가 되긴 하는데, 한 번만 swap한 것과 결과가 다를 수 있어 틀림 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # all nodes in left subtree should be smaller than root value  
    # if not, swap 
    def left_dfs(self, curNode, root):  
        if curNode:
            if curNode.val > root.val:
                curNode.val, root.val = root.val, curNode.val
            
            children = [curNode.left, curNode.right]
            for child in children:
                if child:
                    self.left_dfs(child, root)
    # all nodes in right subtree should be bigger than root value  
    # if not, swap 
    def right_dfs(self, curNode, root):        
        if curNode:
            if curNode.val < root.val:
                curNode.val, root.val = root.val, curNode.val
            
            children = [curNode.left, curNode.right]
            for child in children:
                if child:
                    self.right_dfs(child, root)

    
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.left_dfs(root.left, root)
        self.right_dfs(root.right, root)