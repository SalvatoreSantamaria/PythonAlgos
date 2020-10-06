class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 #left position
        r = len(s)-1 #right position
        while l < r: #going to loop forwards/backwards
          if s[l] == s[r]: #check to see if right and left chars are the same 
            l += 1 #if same increment/decrement
            r -= 1
          else: #if not same, delete either the left char or right char, and see if still palindrome
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
        return True