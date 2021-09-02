def searchInsert(nums: list, target: int) -> int:
    nums.append(target)
    return sorted(nums).index(target)

def solution():
    ls,index = input().split(' ')
    ls = list(int(i) for i in ls.split(','))
    x = searchInsert(ls,int(index))
    print(x)
    
solution()