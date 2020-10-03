class Solution:
    def firstUniqChar(self, s: str) -> int:
        obj = {}
        for i in range (len(s)):
          if s[i] not in obj:
            obj[s[i]] = 1
          else:
            obj[s[i]] += 1
          
        for i in range(len(s)):
          if obj[s[i]] == 1:
            return i
        return -1