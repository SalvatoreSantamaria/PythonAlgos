class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while (left < right):
          s[left], s[right] = s[right], s[left]
          left+= 1
          right-= 1


# also

# def f(x):

#   string = x.strip()
#   string = string[::-1]
#   return string

# print(f('hello'))