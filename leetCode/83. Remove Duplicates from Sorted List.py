# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head):
    cur = head
    if cur == None:
        return head
    while cur.next != None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next  
    return head