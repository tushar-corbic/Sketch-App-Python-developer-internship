

# Question : 'a' is an array where, a[n] > a[n-1]. Given a number P, find the index of P in 'a', if 'a' doesn't have P find the index where a can be inserted satisfying the array condition of a[n] > a[n-1] ?

# Example : a = [1,2,4,5,6]
# when P = 4, the resulting index is 2.
# when P = 7, the resulting index is 5 as that's the only possible place to insert P which satisfies the array condition.
# The objective is to write a python function or a class that takes 2 inputs, 'a' and 'P', and returns the index.



def remainSorted(arr, p):
  """arr->array of sorted numbers
     p-> number to be searched, if not found then have to insert it to the arr

     return-> index of p in arr
  """

  # here I am searching p in the list
  for i in range(len(arr)):
    if(arr[i]==p):
      # if found, index is returned, otherwise the rest of code is executed
      return i
  
  if(len(arr)==0):
    arr.append(p)
    return 0

  # if p is smallest, then it will be inserted at the beginning
  if arr[0]>p:
    arr.insert(0, p)
    return 0

  
  # if p is largest, then it will be inserted at the end
  if(arr[-1]<p):
    arr.append(p)
    return len(arr)-1

  # finding the elment just greater than p and then inserting p before it
  for i in range(len(arr)):
    if(arr[i]>=p):
      arr.insert(i,p)
      return i
