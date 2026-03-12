#(Hash Map / Dictionary)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Zaman Karmaşıklığı: O(n) - Listeyi bir kez dolaşıyoruz.
        Alan Karmaşıklığı: O(n) - Sayıları saklamak için bir sözlük kullanıyoruz.
        """

        dic = {}

        for key, val in enumerate(nums):
            diff = target - val

            if diff in dic:
                return [dic[diff], key]
            
            dic[val] = key  

a = Solution()
a.twoSum([2,7,11,15], 18)  #[1, 2]


#(Brute Force)
from typing import List
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       """
       Zaman Karmaşıklığı: O(n^2) - İç içe iki döngü kullanıldığı için yavaştır.
       Alan Karmaşıklığı: O(1) - Ekstra hafıza kullanılmaz.

       """
       for i in range(len(nums)):
          for j in range(i+1, len(nums)):
             if nums[i] + nums[j] == target:
                return [i, j]

       return []

brute_force = Solution()
brute_force.twoSum([2,7,11,15], 9) #[0, 1]
