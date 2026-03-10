# Problem #1290: Convert Binary Number in a Linked List to Integer
# Zorluk: Easy

"""
    Example 1:
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    
"""

class Solution(object):
    def getDecimalValue(self, head):
        """
        Zaman Karmaşıklığı: O(n) - Listenin her elemanını bir kez ziyaret ediyoruz.
        Alan Karmaşıklığı: O(1) - Sadece tek bir tam sayı değişkeni (sonuc) saklıyoruz.
        
        Mantık: İkili sistemdeki (binary) bir sayıyı onlu sisteme (decimal) çevirirken,
        her yeni basamakta mevcut sonucu 2 ile çarpıp yeni değeri ekleriz.
        """
        current = head
        sonuc = 0

        while current:
            # Bit kaydırma (Bitwise) işlemi ile de yapılabilir: (sonuc << 1) | current.val
            sonuc = (sonuc * 2) + current.val
            current = current.next
            
        return sonuc
