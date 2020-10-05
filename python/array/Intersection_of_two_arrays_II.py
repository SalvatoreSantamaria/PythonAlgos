class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = collections.Counter(nums1) # a = {1:2, 2:2} one appears twice, 2 appears twice
        b = collections.Counter(nums2) # b = {2:2} two appears twice
        
        return (a&b).elements() #elements will return the key and value(aka the frequency)