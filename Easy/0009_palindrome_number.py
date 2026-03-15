"""
Zaman Karmaşıklığı (Time Complexity): O(n)
Alan Karmaşıklığı (Space Complexity): O(n)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        palindrom = []

        for i in str(x):
            palindrom.append(i)

        ters_palindrom = palindrom.copy()
        ters_palindrom.reverse()

        return palindrom == ters_palindrom
