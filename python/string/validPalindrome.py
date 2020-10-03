#both of these output lowercase and letters only cleaned strings

#testing simple words like 'racecar'

def valid_pal(s):
  result = ""
  for i in s:
    if i.isalnum():
      result = i.lower() + result
  print(result)

  if result == s:
    print(True)
  else: 
    print(False)

#valid_pal('racecar')
#valid_pal('hello')

#testing complex sentences like
def valid_pal(s):
  reversed = ""
  for i in s:
    if i.isalnum():
      reversed = i.lower() + reversed
  print(reversed)

  cleanstring = ""
  for i in s:
    if i.isalnum():
      cleanstring = cleanstring + i.lower()
  print(reversed)

  if reversed == cleanstring:
    print(True)
  else: 
    print(False)

valid_pal('A man, a plan, a canal: Panama')
valid_pal('RACECAR')