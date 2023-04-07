# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def buildTestCase(_l1: list,_l2:list) :
    l1_h:ListNode = None
    l1_cur:ListNode = None
    l2_h:ListNode = None
    l2_cur: ListNode = None
    for i in _l1 :
        if(l1_h == None):
            l1_h = ListNode(i,None)
            l1_cur = l1_h
        else:
            l1_cur.next = ListNode(i,None)
            l1_cur = l1_cur.next
    for i in _l2 :
        if(l2_h == None):
            l2_h = ListNode(i,None)
            l2_cur = l2_h
        else:
            l2_cur.next = ListNode(i,None)
            l2_cur = l2_cur.next
    return l1_h, l2_h    
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        h2 = l2
        carry = 0
        result: ListNode = None
        result_head = None
        while h1!=None and h2!=None:
            sum = h1.val + h2.val + carry
            carry = sum//10
            value = sum%10
            if result_head == None :
                result_head = ListNode(value,None)
                result = result_head
            else:
                result.next = ListNode(value,None)
                result = result.next
            print(f'{h1.val}  {h2.val} => {result.val}')
            h1 = h1.next
            h2 = h2.next
        while h1 != None :
            sum = h1.val + carry
            carry = sum//10
            value = sum%10
            result.next = ListNode(value,None)
            print(f'{h1.val}    => {result.next.val}')
            result = result.next
            h1 = h1.next
        while h2 != None :
            sum = h2.val + carry
            carry = sum//10
            value = sum%10
            result.next = ListNode(value,None)
            print(f'   {h2.val} => {result.next.val}')
            result = result.next 
            h2 = h2.next
        if carry :
            result.next = ListNode(carry,None)
            result = result.next
            print(f'     => {result.val}')
        return result_head
            

            

l1,l2 = buildTestCase([9,9,9],[9,9])
solution = Solution()
result = solution.addTwoNumbers(l1,l2)
while result != None :
    print(result.val)
    result = result.next
    
    
    