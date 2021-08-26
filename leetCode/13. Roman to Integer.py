def romanToInt(s: str) -> int:
    # M CM XC IV
    ans = 0
    tmp = -99
    table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in s[::-1]:
        # print(i+':'+str(table[i]),end=' ')
        if tmp == 0:
            tmp = table[i]
        if tmp > table[i]:
            tmp = -99
            ans -= table[i]
        else:
            ans += table[i]
            tmp = table[i]
    return ans

def solution():
    if __name__ == '__main__':
        inpt = input()
        print(romanToInt(inpt))
        
__name__ = '__main__'
solution()
        