def lengthOfLastWord(s: str) -> int:
    stop = False
    counting = False
    count = 0
    for i in s[::-1]:
        if i != " " and not stop:   
            if counting == False :
                counting = True
            if counting == True :
                count += 1
                continue
        else :
            if not stop and counting:
                counting = False
                stop = True
                exit
    return count


def solution():
    inpt = input()
    x = lengthOfLastWord(inpt)
    print(x)
    
def test():
    inpt = input()
    print(inpt[::-1])

solution()
# test()