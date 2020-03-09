#線形探索
def linear_search(l=[], target):
  if len(l) == 0:
    return False
  
  for i in range(len(l)):
    if l[i] == target:
      return True
  
  return False