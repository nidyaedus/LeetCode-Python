class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
            
        uzunluk_h = len(haystack)
        uzunluk_n = len(needle)
        
        for i in range(uzunluk_h - uzunluk_n + 1):
            
            pencere = haystack[i : i + uzunluk_n]
            
            if pencere == needle:
                return i
                
        return -1
