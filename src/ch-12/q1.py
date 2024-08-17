
def add_until_100(array):
  if len(array) == 0:
    return 0 
  total = add_until_100(array[1, len(array) - 1])
  if array[0] + total > 100:
    return total
  else:
    return array[0] + total