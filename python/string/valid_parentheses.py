class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(","}":"{","]":"["} #dictionary with matching closed brackets
        
        for p in s:
          if p in lookup.values():
            stack.append(p) #check to see if it is open, otherwise it is a closed parens/bracket
          elif stack and lookup[p] == stack[-1]: #make sure types are the same
            stack.pop() #if it equals it then pop it off
          else:
            return False #otherwise this is not valid
        return stack == [] #return if stack is empty or not, if not, this is false

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true