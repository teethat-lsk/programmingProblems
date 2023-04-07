import re
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans: int = 0
        pattern = r'^(?!.*(.).*\1)[a-zA-Z0-9]+$'
        re.match(pattern,s)
        length = len(s)
        subString = s[:length]
        
        return ans

    def finder(str,len) :
        subString = str

solution = Solution()
solution.lengthOfLongestSubstring("hello")