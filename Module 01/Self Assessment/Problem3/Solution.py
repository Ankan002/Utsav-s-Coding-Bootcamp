class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        newStringList = [None]*len(indices)

        startingPoint = 0
        endingPoint = len(indices) - 1

        while(startingPoint <= endingPoint):
            if startingPoint == endingPoint:
                newStringList[int(indices[startingPoint])] = s[int(startingPoint)]
                startingPoint += 1
                endingPoint -= 1
                continue

            newStringList[int(indices[startingPoint])] = s[int(startingPoint)]
            newStringList[int(indices[endingPoint])] = s[int(endingPoint)]

            startingPoint += 1
            endingPoint -= 1

        return "".join(newStringList)


solution = Solution()
print(solution.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(solution.restoreString("abc", [0,1,2]))
print(solution.restoreString("aiohn", [3,1,4,2,0]))
print(solution.restoreString("aaiougrt", [4,0,2,6,7,3,1,5]))
print(solution.restoreString("art", [1,0,2]))