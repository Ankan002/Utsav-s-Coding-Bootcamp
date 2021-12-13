class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stringList = list(s)

        startingPoint = 0
        endingPoint = len(stringList) - 1

        while(startingPoint <= endingPoint):
            if not str.isalpha(stringList[startingPoint]) and not str.isalpha(stringList[endingPoint]):
                startingPoint += 1
                endingPoint -= 1

            elif not str.isalpha(stringList[startingPoint]) and str.isalpha(stringList[endingPoint]):
                startingPoint += 1

            elif str.isalpha(stringList[startingPoint]) and not str.isalpha(stringList[endingPoint]):
                endingPoint -= 1

            else: 
                self.__swap(stringList, startingPoint, endingPoint)
                startingPoint += 1
                endingPoint -= 1

        return "".join(stringList)

    def __swap(self, stringList: list[str], firstIndex: int, endPoint: int) -> None:
        temp = stringList[firstIndex]
        stringList[firstIndex] = stringList[endPoint]
        stringList[endPoint] = temp


solution = Solution()
print(solution.reverseOnlyLetters("ab-cd"))
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))