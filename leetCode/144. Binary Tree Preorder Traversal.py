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
        ans.append(cur.val)
        solution(cur.left)
        solution(cur.right)
    return ans
class Solution:
    def preorderTraversal(self, root):
        global ans
        ans = []
        return solution(root)
        