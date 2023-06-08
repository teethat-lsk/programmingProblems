class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        _set = set(nums)
        return len(_set) < len(nums)
    
solution = Solution()
inp = input()
print(solution.containsDuplicate(inp.split(' ')))