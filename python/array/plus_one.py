class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      digits = list(map(str, digits)) #turn all digits into a string and then back into a list of strings ['1','2', '3']
      digits = ''.join(digits) #join them to make '123'
      digits = str(int(digits) + 1) #change to a number and add 1 and then back into a str
      digits = list(digits) #change it back to an arr (its now an array of strings)
      return list(map(int, digits)) #make arr of strings into arr of numbers

# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.