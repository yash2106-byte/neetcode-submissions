class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        if len(a) != len(b):
            return False
        j = 0
        for i in a:
            if i != b[j] :
                return False
            j+=1
        return True
        