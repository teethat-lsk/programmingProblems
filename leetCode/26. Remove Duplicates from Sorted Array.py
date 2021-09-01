def removeDuplicates(nums): 
    mxlen = len(nums)
    index = 0
    count = 1
    if mxlen <= 1:
        return mxlen
    while index < mxlen-1:
        if nums[index] != nums[index+1]:
            index+=1
            count+=1
        else:
            nums.pop(index+1)
            mxlen -= 1
        
    return count
            

def solution():
    inpt = input().split(' ')
    x = removeDuplicates(inpt)
    print(inpt,x)


def test():
    a = [1,2,3,3,3,3]
    b = set(a)
    print(b)

solution()
# test()