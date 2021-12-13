class Solution: 
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return False

        numberSet = set()

        for num in nums:
            if num in numberSet:
                return True

            numberSet.add(num)

        return False


solution = Solution()

print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))