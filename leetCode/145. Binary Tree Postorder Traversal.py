# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solution(root):
    global ans
    cur = root
    if cur == None:
        return 
    if cur != None:
        
        solution(cur.left)
        solution(cur.right)
        ans.append(cur.val)
    return ans
class Solution:
    def postorderTraversal(self, root):
        global ans
        ans = []
        return solution(root)