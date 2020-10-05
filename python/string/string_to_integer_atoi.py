class Solution:
    def myAtoi(self, s: str) -> int:
        str = s
        str = str.lstrip() #remove whitespace
        if not str: #if string in empty
          return 0
        if str[0] not in "+-0123456789":
          return 0
        if str[0] in "+-":
          if len(str) == 1:
            return 0
          elif str[1].isdigit() == False: #if second character is not a digit
            return 0
        if str[0] == "-": #if char is neg
          sign = -1
        else: 
          sign = 1
        
        #strip the string of =/-
        str = str.lstrip("+")
        str = str.lstrip("-")
        
        i = 0
        result = ""
        while i < len(str) and str[i].isdigit(): #while in range and counter is a digit
          result += str[i]
          i += 1
        result_int = int(result) #convert string to integer
        result_int = result_int * sign
        
        #edge case to check if in boundaries
        if result_int > 2**31 - 1:
          return 2**31 - 1
        elif result_int < -2**31:
          return -2**31 
        else:
          return result_int

# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered a whitespace character.
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
 

# Example 1:

# Input: str = "42"
# Output: 42
# Example 2:

# Input: str = "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
# Example 3:

# Input: str = "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.