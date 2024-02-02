
# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

#Method1
def front_back(str):
  n = len(str)
  if n>2:
    return str[-1]+str[1:-1]+str[0]
  else:
    return str[::-1] 

#Method2
def front_back(str):
  if(len(str)>1):
    return str[len(str)-1] + str[1:len(str)-1] + str[0]
  return str

