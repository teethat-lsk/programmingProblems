# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

leftTree = []
rightTree = []

def buildLeft(root):
    global leftTree
    cur = root
    if cur == None:
        leftTree.append(-101)
        return 
    if cur != None:
        leftTree.append(cur.val)
        buildLeft(cur.left)
        buildLeft(cur.right)
    return leftTree

def buildRight(root):
    global rightTree
    cur = root
    if cur == None:
        rightTree.append(-101)
        return 
    if cur != None:
        rightTree.append(cur.val)
        buildRight(cur.right)
        buildRight(cur.left)
    return rightTree

class Solution:
    def isSymmetric(self, root):
        global rightTree
        global leftTree
        leftTree = []
        rightTree = []
        l = buildLeft(root.left) 
        r = buildRight(root.right)
        # print(l,r)
        return l == r
        
            