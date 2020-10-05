#output with print()

#make a hashmap


#for loop #################################################################### for loop
#loop over characters in a string
s = 'string'
for i in s:
  print(i) #prints s t r i n g 

#loop over index in a string
for i in range(0, len(s)):
  print(i) #prints 0 1 2 3 4 5

#loop over an array aka list
arr = ['a','r','r']
for i in arr:
  print(i) #prints a r r

#loop over index in an arr
for i in range(0, len(arr)):
  print(i) #prints 0 1 2
  print(arr[i]) #prints a r r

#loop over object #aka dictionary
obj = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in obj:
  print(key) #prints color fruit pet

for key in obj:
  print(obj[key])#prints blue apple dog

print(obj.items()) #prints dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

#converstions ################################################################ converstions

string = "123"
  #string to int 
    print(int(string))
    #prints 123

  #string to array 
    print(list(string)) also string.split(',')
    #prints ['1','2','3']

  #string to hashmap
  obj = {}
  for i in range (len(s)):
    if s[i] not in obj:
      obj[s[i]] = 1
    else: 
      obj[s[i]] += 1
    #obj is {'1': 1, '2': 1, '3': 1}


integer = 123
  #int to string
    print(str(integer))

  #int to array
    string = str(integer)
    arr = list(string)
    print(arr)
    #prints ['1','2','3']

arr = ['1','2','3']
  #array to string
  str1 = ''
  print(str1.join('arr'))
  #prints 123
