"""
Zaman Karmaşıklığı (Time Complexity): O(n). Listenin üzerinden sadece bir kere geçildi.
Alan Karmaşıklığı (Space Complexity): O(1). İki tane değişken (yazici ve okuyucu) kullanarak orijinal listeyi kendi içinde (in-place) değiştirildi. 

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        yazici = 1

        for okuyucu in range(1, len(nums)):
            if nums[okuyucu] != nums[okuyucu -1]:
                nums[yazici] = nums[okuyucu]
            
                yazici += 1
        return yazici
