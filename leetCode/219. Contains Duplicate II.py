class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        posMap = {}
        for pos,val in enumerate(nums) :
            if val in posMap:
                if int(pos) - int(posMap[val]) <= int(k) :
                    return True
            posMap[val] = pos
        else :
            return False


inp,k = input("test case : ").split("|")
solution = Solution()
print(solution.containsNearbyDuplicate(inp.split(" "),k))
    
    