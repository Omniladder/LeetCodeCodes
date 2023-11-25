class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        indexStorage = {}
        for i in range(len(nums)):
            if target - nums[i] not in indexStorage:
                indexStorage[nums[i]] = i
            else:
                indexes.append(i)
                indexes.append(indexStorage.get(target - nums[i]))
                return indexes
        