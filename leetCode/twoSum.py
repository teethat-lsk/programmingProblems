
def twoSum(nums,target):
    ans = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if int(nums[i])+int(nums[j]) == int(target) :
                ans.append(i)
                ans.append(j)
                return ans
def twoSum_butFaster(nums, target) :
        D = {}
        
        for i in range(len(nums)):
            temp = int(target)-int(nums[i])
            if temp in D:
                return [i, D[temp]]
            else:
                D[nums[i]] = i
            
    
def solution():
    if __name__ == "__main__":
        print("running...")
        tmp , target = input().split(" ")
        tmp = tmp.split(",")
        num = [int(x) for x in tmp]
        print(num)
        print(target)    
        print(twoSum(num,target))

   
__name__ = "__main__"           
solution() 
        
                    