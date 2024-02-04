
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

#Method1
def array_front9(nums):
  count = 0
  for i in nums[0:4]:
    if(i==9):
      count+=1
  if count>0:
    return True
  return False

#Method2
def array_front9(nums):
  for i in range(min(4,len(nums))):
    if nums[i]==9:
      return True
  return False
