class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        posMap = {}
        for currentPos,val in enumerate(nums) :
            if val in posMap :
                for pos in posMap[val] :
                    if abs( currentPos - pos) <= indexDiff:
                        return True
                tmp = [int(currentPos)]
                tmp.extend(posMap[val])
                posMap[val] = tmp
            else :
                posMap[i] = [int(currentPos)]
        return False       
    
    
inDiff,valDiff = input("test case : ").split(" ")   
solution = Solution()
print(solution.containsNearbyAlmostDuplicate([1,2,3,1],int(inDiff),int(valDiff)))