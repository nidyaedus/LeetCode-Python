"""
Zaman Karmaşıklığı: O(n). Metin uzunluğu kadar sadece bir kere dönüyoruz. Sözlükte arama yapmak ve yığından eleman çekmek/eklemek O(1) sürede gerçekleşiyor.
Alan Karmaşıklığı: O(n). En kötü senaryoda (örneğin metin (((((( gibi sadece açılış parantezlerinden oluşuyorsa) tüm karakterleri yığına ekleriz, bu da bellek kullanımının metnin uzunluğuyla doğru orantılı olmasını sağlar.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        stck = []
        sozluk = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for karakter in s:
            
            if karakter in sozluk:
                
                en_ustteki_eleman = stck.pop() if stck else '#'
                
                if en_ustteki_eleman != sozluk[karakter]:
                    return False
                    
            else:
                
                stck.append(karakter)
                
        return len(stck) == 0  
