# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solution(self,root,targetsum,summ):
        if not root.left and not root.right:
            if summ == targetsum:
                print('true from leaf')
                return True
            print('false from leaf')
            return False
        summ += root.val
        print(summ)
        if self.solution(root.left,targetsum,summ) or self.solution(root.right,targetsum,summ):
            print('true')
            return True
        print('false')
        return False
        
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root :
            return False
        if (not root.left and not root.right)  and targetSum == root.val:
            return True
        if (not root.left or not root.right)  and targetSum == root.val:
            return False
        return self.solution(root,targetSum,0)
            
        