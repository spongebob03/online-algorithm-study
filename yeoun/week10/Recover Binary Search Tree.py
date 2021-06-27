# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result, swap = self.inorder(root, result=[], swap=[])
        # swap의 첫 번째 값과 마지막 값을 서로 교환 
        swap[0].val, swap[-1].val = swap[-1].val, swap[0].val

    
    # inorder traversal
    def inorder(self, root, result, swap):
        node = root
        if node:
            # 왼쪽 자식
            if node.left:
                result, swap = self.inorder(node.left, result, swap)
            # 대소관계 맞지 않으면 swap에 저장 
            if result and result[-1].val >= node.val:
                swap += [result[-1], node]
            # 루트
            result.append(node)
            # 오른쪽 자식 
            if node.right:
                result, swap = self.inorder(node.right, result, swap)
        return result, swap
        