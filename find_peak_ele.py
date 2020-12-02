def findPeak(nums):
  
  if len(nums) == 1:
    return 0
  
  
	for i in range(0, len(nums)):
      if i == 0:
        if nums[i] > nums[i+1]:
          return i
      elif i == len(nums)-1:
        if nums[i] > nums[i-1]:
          return i
      elif i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
          return i
  
  


#ruby
# # O(log n) Solution - uses recursive BSearch
def find_peak_element(nums)
    return b_search(nums, 0, nums.length - 1)    
end

def b_search(nums, l, r)        # 0, 3
    if l==r
        return l
    end
    
    mid = (l + r) / 2           # 1         #2
    if nums[mid] > nums[mid+1]      # 2>3       #3>1
        return b_search(nums, l, mid)           #2, 2
    else
        return b_search(nums, mid+1, r)     #2,3
    end
 
end