def isValid(s: list) -> bool:
    stack = []
    pair = {')':'(',']':'[','}':'{'}
    if len(s) > 10**4 or len(s) < 1:
        return False
    for i in s:
        # print(stack,'<====>',i,end = "  ------> ")
        if len(stack) == 0 :
            stack.append(i)
            # print(stack)
            continue
        if i in pair:
            if stack[-1] == pair[i]:
                stack.pop()
                # print(stack)
                continue

        stack.append(i)
        # print(stack)
    if len(stack):
        return False    
    return True

def solution():
    inpt = input().split(' ')
    print(isValid(inpt))
    
solution()
    
    