class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a = sorted(s)
        # b = sorted(t)
        # if len(a) != len(b):
        #     return False
        # j = 0
        # for i in a:
        #     if i != b[j] :
        #         return False
        #     j+=1
        # return True
        
        a = sorted(s)
        b = sorted(t)
        if len(a) != len(b):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char,0)+1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
        return all(values==0 for values in count.values())