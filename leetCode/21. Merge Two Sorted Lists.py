# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    lis1 = []
    lis2 = []
    while l1 != None:
        lis1.append(l1.val)
        l1 = l1.next
    while l2 != None:
        lis2.append(l2.val)
        l2 = l2.next
    for i in lis2:
        lis1.append(i)
    lis1 = sorted(lis1)
    if len(lis1) != 0:
        head = ListNode(lis1[0])
    else :
        return 
    
    cur = head
    for i in lis1[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


def solution():
    l1,l2 = input().split(" ")
    l1 = list(i for i in l1)
    l2 = list(i for i in l2)
    print(l1,l2)
    print(mergeTwoLists(l1,l2))
    
solution()