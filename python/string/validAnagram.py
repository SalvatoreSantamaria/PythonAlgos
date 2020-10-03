class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      obj = {}
      objt = {}
      for i in range (len(s)):
        if s[i] not in obj:
          obj[s[i]] = 1
        else: 
          obj[s[i]] += 1

      for i in range (len(t)):
        if t[i] not in objt:
          objt[t[i]] = 1
        else: 
          objt[t[i]] += 1

      return(obj == objt)

valid_a('hi', 'ith')