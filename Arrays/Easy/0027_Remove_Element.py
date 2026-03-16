"""
Zaman Karmaşıklığı: O(n). Tüm listeyi sadece bir kez for döngüsü ile gezildi.
Alan Karmaşıklığı: O(1). Mevcut listenin üzerine yazarak bellekten tasarruf edildi.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        yazici = 0
        
        for okuyucu in range(len(nums)):
            
            if nums[okuyucu] != val:
                
                nums[yazici] = nums[okuyucu]

                yazici += 1
                
        return yazici
