def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    if n == 0:
        return
    if m == 0:
        for i in range(n):
            nums1.pop()
        nums1.extend(nums2)
        return 
    if m == 1 and n == 1:
        nums1.pop()
        if nums1[0] > nums2[0]:
            nums1.insert(0,nums2[0])
        else:
            nums1.append(nums2[0])
        
        return
    temp = nums1[:m]
    temp.extend(nums2)
    temp = sorted(temp)
    index = 0
    while index < m+n:
        # print(temp)
        # print(nums1)
        if nums1[index] != temp[index]:
            nums1.insert(index,temp[index])
        index += 1
    while len(nums1) > m+n:
        nums1.pop()
def test(nums):
    nums.append(sorted(nums))

def solution():
    inpt = input().split(",")
    nums1 = inpt[0].split(' ')
    nums2 = inpt[2].split(' ')
    merge(nums1,int(inpt[1]),nums2,int(inpt[3]))
    print(nums1)

solution()