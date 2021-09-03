def plusOne(digits: list):
    a = ''
    for i in digits:
        a += str(i)
    a = str(int(a)+1)
    return list(map(int,list(i for i in a)))

def solution():
    inpt = list(map(int,input().split(' ')))
    x = plusOne(inpt)
    print(x)

def test():
    a = '123'
    a = str(int(a)+1)
    print(a)
solution()
# test()
    