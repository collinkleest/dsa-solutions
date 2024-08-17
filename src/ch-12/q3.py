

def unique_paths(rows: int, columns: int, mem: dict):
  if rows == 1 or columns == 1:
    return 1
  
  if not mem.get([rows, columns]):
    mem[[rows, columns]] = unique_paths(rows - 1, mem) + unique_paths(rows, columns - 1, mem)
  
  return mem[[rows, columns]]