"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
ans = []
def solution(root):
    global ans
    cur = root
    if cur == None:
        return
    
    if cur.children != None:
        for i in cur.children:
            solution(i)
    ans.append(cur.val)
    return ans
class Solution:
    def postorder(self, root):
        global ans
        ans = []
        return solution(root)