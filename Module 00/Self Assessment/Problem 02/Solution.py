class Solution:
    def generate(self, numRows: int) -> list[list[int]]: 
        pascalsTriangle = []

        for i in range(numRows):
            subPart = []
            for j in range(i+1):
                if (j==0) or (j==i):
                    subPart.append(1)
                else:
                    subPart.append(pascalsTriangle[i-1][j-1]+pascalsTriangle[i-1][j])

            pascalsTriangle.append(subPart)

        return pascalsTriangle


solution = Solution()

print(solution.generate(5))
print(solution.generate(1))