
# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]

#Method1
def reverse3(nums):
  result = []
  for i in range(len(nums)):
    result.insert(0,nums[i])
  return result
#Method2  
def reverse3(nums):
  return nums[::-1]
