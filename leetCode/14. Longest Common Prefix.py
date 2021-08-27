def test() :
    print ('a' != 'asdf')

def longestCommonPrefix(strs):
    output = ""
    strs = sorted(strs, key=len)
    print (strs)
    length = len(strs[0])
    for letInd in range(length):
        for string in strs:
            if strs[0][letInd] != string[letInd]:
                return output
        output += string[letInd]
    return output     

def solution():
    if __name__ == '__main__':
        ls = input().split(',')
        print(longestCommonPrefix(ls))
          
__name__ = '__main__'
solution()
# test()

        
