class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        YAKLAŞIM: Hash Map ile Harf Frekanslarını Sayma
        Zaman Karmaşıklığı: O(n) - Kelimeleri sadece bir kez geziyoruz.
        Alan Karmaşıklığı: O(1) - Sözlükler en fazla 26 karakter tutacağı için sabit bir alan kaplar.
        """
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT
