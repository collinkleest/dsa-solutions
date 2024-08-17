

def golamb(n: int, mem: dict):
  if n == 1:
    return 1
  
  if not mem.get(n):
    mem[n] = 1 + golamb(n - golamb(n - golamb(n - 1, mem), mem), mem)

  return mem.get(n)