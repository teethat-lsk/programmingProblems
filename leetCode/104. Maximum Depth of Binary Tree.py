# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def goingDown(root,count):
        if root == None:
            # print("not root")
            return count

        leftDepth = goingDown(root.left,count)
        rightDepth = goingDown(root.right,count)
        if leftDepth >= rightDepth:
            count += leftDepth
        elif leftDepth < rightDepth:
            count += rightDepth
        return count+1
        
            

class Solution:
    def maxDepth(self, root) -> int:
        return goingDown(root,0)
    