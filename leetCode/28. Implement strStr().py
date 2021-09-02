def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    if n == 0:
        return 0
    ans = -1
    for i in range(len(haystack)-n+1):
        if haystack[:n] == needle:
            ans = i 
            break
        else:
            haystack = haystack[1:]
    return ans            

def test():
    a = 'abcsdfghijk'
    for i in a:
        if i == 'p':
            break          
    else:
        print(a)
        
def solution():
    hay,needle = input().split(" ")
    x = strStr(hay,needle)
    print(x)

# test()   
solution()