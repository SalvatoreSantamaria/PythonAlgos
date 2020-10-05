class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        next_non_zero = 0 #keep track of index position
        
        for n in nums:
          if n != 0: #make a swap when not a zero
            nums[next_non_zero] = n #insert n in to next_non_zero index position
            next_non_zero += 1 #increment to move to next spot
        for zero in range(1, zero_count + 1): #go all the way up to and including the zero count
          nums[-zero] = 0  #counting backwards

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.