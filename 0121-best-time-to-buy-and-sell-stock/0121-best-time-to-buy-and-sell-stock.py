class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitbyDay = [0] * len(prices)
        #print(len(profitbyDay))
        minCost = prices[0]
        for i in range(len(prices)):
            if minCost > prices[i]:
                minCost = prices[i]
            profitbyDay[i] = prices[i] - minCost
        
        return max(profitbyDay)
            
        