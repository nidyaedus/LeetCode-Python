"""
        Zaman Karmaşıklığı: O(n) - set() fonksiyonu arka planda tüm listeyi dönerek O(n) zaman harcar.
        Alan Karmaşıklığı: O(n) - Yeni bir set objesi oluşturulur.
        
        Mantık: sets tekrar eden (duplicate) eleman barındırmazlar.
        Eğer orijinal listenin uzunluğu ile, o listenin kümeye dönüştürülmüş halinin uzunluğu farklıysa,
        arada tekrar eden elemanlar var demektir.
        """

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) != len(nums)
    
