def maxSubArray(nums: list) -> int:
    if len(nums) <= 1:
        return nums[0]
    cur = 0
    # print(((cur := max(num, cur + num)) for num in nums ))
    return max( (cur := max(num, cur + num)) for num in nums )


def solution():
    inpt = list(int(i) for i in input().split(','))
    x = maxSubArray(inpt)
    print(x)
    
def test():
    a = [1,2,3,4]
    print(list(x+1 for x in a))

    
solution()
# test()