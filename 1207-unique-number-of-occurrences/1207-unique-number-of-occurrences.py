class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurenceMap = {}
        for i in arr:
            if i not in occurenceMap:
                occurenceMap[i] = 1
            else:
                occurenceMap[i] += 1
        
        timesMap = set()
        checkSet = set()
        
        for i in arr:
            if i not in checkSet:
                if occurenceMap[i] in timesMap:
                    return False
                else:
                    timesMap.add(occurenceMap[i])
                    checkSet.add(i)
        return True