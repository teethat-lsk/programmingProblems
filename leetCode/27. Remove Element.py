def removeElement(nums: list, val: int) -> int:
    mxlen = len(nums)
    index = 0
    if mxlen == 1:
        if int(nums[0]) == val:
            return index
    for i in range(mxlen):
        if int(nums[i]) != val:
            nums[index] = nums[i]
            index += 1
    return index

def removeElement_x(nums: list, val: int) -> int:
    nums.sort()
    count = 0
    for i in nums:
        if int(i) == val:
            count += 1
            
    for i in range(count):
        nums.remove(str(val))
        print(nums)
            
    return len(nums)
    
def solution():
    inpt, val = input().split(',')
    inpt = inpt.split(' ')
    x = removeElement_x(inpt,int(val))
    print(inpt,x)


solution()
     