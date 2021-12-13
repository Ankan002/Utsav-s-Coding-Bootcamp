class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for character in s:
            if str.isalnum(character):
                newString += character.lower()

        return newString == self.__reverseString(newString)

    def __reverseString(self, s: str) -> str:
        characterList = list(s)

        startingPoint = 0
        endingPoint = len(characterList) - 1

        while(startingPoint <= endingPoint):
            temp = characterList[startingPoint]
            characterList[startingPoint] = characterList[endingPoint]
            characterList[endingPoint] = temp
            startingPoint += 1
            endingPoint -= 1

        return "".join(characterList)


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))