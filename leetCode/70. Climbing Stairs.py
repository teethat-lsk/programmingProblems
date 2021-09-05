data = [1,1,2] + [-1]*50
def recur(n):
    if data[n] == -1:
        data[n] = recur(n-1)+recur(n-2)
        return data[n]
    else:
        return data[n]
def climbStairs(n: int) -> int:
    return recur(n)
    

def solution():
    inpt = input()
    x = climbStairs(int(inpt))
    print(x)

solution()

# 3

# 5 
# 1 1 1 1 1
# 
# 1 1 1 2
# 1 1 2 1
# 1 2 1 1
# 2 1 1 1
# 
# 1 2 2
# 2 1 2
# 2 2 1

# 7 
# 1 1 1 1 1 1 1
# 
# 1 1 1 1 1 2
# 1 1 1 1 2 1
# 1 1 1 2 1 1
# 1 1 2 1 1 1
# 1 2 1 1 1 1
# 2 1 1 1 1 1

# 2 2 1 1 1
# 1 1 1 2 2
# 2 1 2 1 1
# 1 1 2 1 2
# 2 1 1 2 1
# 1 2 1 1 2
# 2 1 1 1 2
# 1 2 2 1 1
# 1 1 2 2 1
# 1 2 1 2 1

# 2 2 2 1
# 1 2 2 2
# 2 1 2 1 1
# 1 1 2 1 2
# 2 1 1 2 1
# 1 2 1 1 2
# 2 1 1 1 2
# 1 2 2 1 1
# 1 1 2 2 1
# 1 2 1 2 1







# 2 2 2 1

# 1 2 2
# 2 1 2
# 2 2 1


# 3
# 1 1 1
# 1 2
# 2 1
