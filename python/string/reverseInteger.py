def reverse_integer(x):
  # get a string from absolute value of x
  string = str(abs(x))

  #string leading zeros 
  string = string.strip()

  #reverse string 
  string = string[::-1]

  # convert output back into int
  output = int(string)

  # make sure output is in range
  if output >= 2**31 -1 or output <= -2**31:
    return 0
  elif x < 0: #if x is negative
    return -1 * output
  else: 
    return output

print(reverse_integer(1230)) 