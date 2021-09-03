def addBinary(a: str, b: str) -> str:
    ans = bin(int(a,2) + int(b,2)) 
    return ans[2:]

def solution():
    a,b = input().split(' ')
    x = addBinary(a,b)
    print(x)
    
solution()