class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        rightSum = 0
        for i in nums:
            rightSum += i
        leftSum = 0

        output = [0] * len(nums)

        for i in range(len(nums)):
            
            output[i] = nums[i] * i - leftSum + rightSum - nums[i] * (len(nums) - i)

            rightSum -= nums[i]
            leftSum += nums[i]
        return output