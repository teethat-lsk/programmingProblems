def isPerfectSquare(num: int) -> bool:
    itis = True
    sqr  = num**0.5
    if sqr > int(sqr):
        itis = False
    return itis

def solution():
    inpt = int(input())
    x = isPerfectSquare(inpt)
    print(x)
    
def test():
    a = 1.05
    b = int(1)
    print (a>b)
    
    
solution()
# test()