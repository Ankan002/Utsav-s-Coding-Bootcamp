class Solution:
    def reorderSpaces(self, text: str) -> str:
        numberOfSpaces = 0

        startingPoint = 0
        endingPoint = len(text) - 1

        while(startingPoint <= endingPoint):
            if startingPoint == endingPoint:
                if text[startingPoint] == " ":
                    numberOfSpaces += 1

                startingPoint += 1
                endingPoint -= 1
                continue

            if text[startingPoint] == " ":
                numberOfSpaces += 1

            if text[endingPoint] == " ":
                numberOfSpaces += 1

            startingPoint += 1
            endingPoint -= 1

        if numberOfSpaces == 0:
            return text

        stringArray = text.split(" ")
        startingPoint = 0
        endingPoint = len(stringArray) - 1

        while startingPoint <= endingPoint:
            if stringArray[startingPoint] == "":
                stringArray.pop(startingPoint)
                endingPoint -= 1
            else: 
                startingPoint += 1

        if len(stringArray) == 1:
            return "".join(stringArray) + " "*numberOfSpaces
        
        return (" "*(numberOfSpaces//(len(stringArray) - 1))).join(stringArray) + " "*(numberOfSpaces%(len(stringArray) - 1))


solution = Solution()
print(solution.reorderSpaces("  this   is  a sentence "))
print(solution.reorderSpaces(" practice   makes   perfect"))
print(solution.reorderSpaces("hello   world"))
print(solution.reorderSpaces("  walks  udp package   into  bar a"))
print(solution.reorderSpaces("a"))
print(solution.reorderSpaces("  hello"))