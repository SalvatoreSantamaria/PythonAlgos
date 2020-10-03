class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # cant be any duplicates
        if len(nums) < 2:
          return False
        # collections will create a dictionary
        dictionary = collections.Counter(nums)
        
        #.most_common(1)[0][1] is going to create a tuple of key value pairs
        return dictionary.most_common(1)[0][1] >= 2



Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true