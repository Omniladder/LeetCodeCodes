class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = Counter()

        if len(s) != len(t):
            return False


        for i in s:
            hashSet.update([i])
        


        for i in t:
            if i in hashSet and hashSet[i] > 0:
                hashSet.subtract([i])
            else:
                return False
        return True
        