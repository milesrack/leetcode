class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        for l in set(ransomNote):
            if ransomNote.count(l) > magazine.count(l):
                return False
        return True

