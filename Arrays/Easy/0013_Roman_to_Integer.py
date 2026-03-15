 
class Solution:
"""Zaman Karmaşıklığı (Time Complexity): O(n). String'in uzunluğu n kadar olduğu için sadece bir kere dönüyoruz."""
"""Alan Karmaşıklığı (Space Complexity): O(1). Sözlük sabit 7 elemanlı olduğu ve ekstra liste oluşturmadığımız için bellekte ekstra yer kaplamıyor.""" 
    
    def romanToInt(self, s: str) -> int:
        
        roman_val = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        
        toplam = 0
        
        for i in range(len(s) - 1):
            
            su_anki_deger = roman_val[s[i]]
            sonraki_deger = roman_val[s[i + 1]]
            
            if su_anki_deger < sonraki_deger:
                toplam -= su_anki_deger
            else:
                toplam += su_anki_deger
                
        toplam += roman_val[s[-1]]  
        
        return toplam
