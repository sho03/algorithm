#return true if target contains list(a)
def binary_search(a=[], target=None):
  a.sort()
  l = 0
  r = len(a) - 1
  while l <= r:
    mid = (r - l) // 2
    if target == a[mid]:
      return True
    
    if target > a[mid]:
      l = mid
    else:
      r = mid
  
  return False