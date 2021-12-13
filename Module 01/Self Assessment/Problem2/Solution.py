class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        startingPoint = 0
        endingPoint = len(s) - 1

        while (startingPoint <= endingPoint):
            temp = s[startingPoint]
            s[startingPoint] = s[endingPoint]
            s[endingPoint] = temp
            startingPoint += 1
            endingPoint -= 1


solution = Solution()

s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]

solution.reverseString(s1)
solution.reverseString(s2)

print(s1)
print(s2)