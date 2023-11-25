class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        numZeros = 0
        product = 1

        for i in nums:
            if i == 0:
                numZeros += 1
            else:
                product *= i
        
        finalAns = []

        for i in nums:
            if numZeros == 1:
                if i != 0:
                    finalAns.append(0)
                else:
                    finalAns.append(product)
            else: 
                if numZeros > 1:
                    finalAns.append(0)
                else:
                    finalAns.append(int(product / i))
        return finalAns