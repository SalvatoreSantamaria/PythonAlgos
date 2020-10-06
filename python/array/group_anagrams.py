class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        #go through list and covert word into a key
        for s in strs: #for each word in string
          key = "".join(sorted(list(s))) #covert intoa list and reconvert into a string
          lookup[key].append(s) #append whatever the string is into the list
        
        output = [] #initialize output
        
        for l in lookup.values(): #for each list inside lookup values
          output.append(l) #just append each list
        
        return output

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]