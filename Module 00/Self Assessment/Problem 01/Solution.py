class Solution:
    def removeDuplicates(self, nums: list[int]) -> int :
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 1

        startPoint = 1
        endPoint = len(nums) - 1

        while startPoint <= endPoint:
            if nums[startPoint - 1] == nums[startPoint]:
                nums.pop(startPoint)
                endPoint -= 1

            else:
                startPoint += 1
        
        return len(nums)


solution = Solution()

print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
