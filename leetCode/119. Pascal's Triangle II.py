triangle = [[1],[1,1]] + [-1]*33
class Solution:
    def getRow(self,numRows):
        global triangle
        if triangle[numRows] != -1:
            return triangle[numRows]
        if triangle[numRows] == -1:
            triangle[numRows] = [-1]*(numRows+1)
        for i in range(numRows+1):
            if i-1 < 0 or i == numRows:
                triangle[numRows][i] = 1
            else:
                triangle[numRows][i] = self.getRow(numRows-1)[i-1] + self.getRow(numRows-1)[i]
                
       
        
        return triangle[numRows]
        
                
        
            
    def test(self):
        x = [1,2]
        x[1] = [-1]*(3+1)
        for i in range(3):
            x[1][i] = 50
        print(x)
       

solution = Solution()

inpt = int(input())
print(solution.generate(inpt))
# solution.test()


        