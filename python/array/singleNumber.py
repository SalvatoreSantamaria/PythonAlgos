class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # make a dictionary
        dic = {}       
        for num in nums:
          if num not in dic:
            dic[num] = 1
          else:
            dic[num] += 1
            
        # search dictionary for the item
        # using key and value, iterate through all of the dic.items
        for key, val in dic.items():
          if val == 1:
            return key

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1