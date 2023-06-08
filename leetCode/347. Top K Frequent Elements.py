class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for i in nums :
            if i in counter : 
                counter[i] += 1
            else :
                counter[i] = 1
        print(counter)
            

inp,k = input("test case : ").split(" ")
solution = Solution()
solution.topKFrequent(list(inp),int(k))