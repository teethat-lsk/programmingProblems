def isPalindrome(x):
    if len(str(x)) == 1:
        return True
    elif x > 0:
        tmp = str(abs(x))
        ofset = len(tmp) % 2   
        halfway = int(len(tmp)/2)
        ll = tmp[:halfway+ofset]
        rl = tmp[:halfway-1:-1]
        if ll == rl:
            return True
    return False

def isPalindrome_faster(x: int) -> bool:
    x=str(x)
    return x == x[::-1] 
    
def solution():
    if __name__ == "__main__":
        inpt = int(input())
        print(isPalindrome(inpt))
        

__name__ = '__main__'
solution()