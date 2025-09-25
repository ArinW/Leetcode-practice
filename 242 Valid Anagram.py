class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        set_s=set(s)
        if len(t)!=len(s):
            return False
        dict_s= {}
        for i in s:
            dict_s[i]=dict_s.get(i,0)+1
        
        for j in t:
            if j not in dict_s or dict_s[j]==0:
                return False
            dict_s[j]-=1
        return True