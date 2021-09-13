triangle = [[1],[1,1]] + [-1]*33
class Solution:
    def build(self,numRows):
        global triangle
        if triangle[numRows] != -1:
            return triangle[numRows]
        if triangle[numRows] == -1:
            triangle[numRows] = [-1]*(numRows+1)
        for i in range(numRows+1):
            if i-1 < 0 or i == numRows:
                triangle[numRows][i] = 1
            else:
                triangle[numRows][i] = self.build(numRows-1)[i-1] + self.build(numRows-1)[i]
             
       
        
        return triangle[numRows]

    def generate(self,num):
        global triangle
        self.build(num)
        return triangle[:num]

solution = Solution()

inpt = int(input())
print(solution.generate(inpt))
