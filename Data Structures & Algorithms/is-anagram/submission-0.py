class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        for ch in s:
            mp1[ch] = mp1.get(ch, 0) + 1

        mp2 = {}
        for ch in t:
            mp2[ch] = mp2.get(ch, 0) + 1

        return mp2 == mp1