class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if len(strs) == 0:
        return ("")
      if len(strs) == 1:
        return(strs[0])
      
      pref = strs[0] #prefix
      plen = len(pref) #prefixlength
      
      for s in strs[1:]: #looping through the input array starting at strs[1]
        while pref != s[0:plen]: #while prefix doesnt exist in the numbers of letters
          pref = pref[0:(plen-1)] #shorted the prefix and cutoff last char
          plen -= 1
          
          if plen == 0:
            return("")
          
      return(pref)

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.