def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a)< len(b):
    if b[len(a)*-1:]== a:
      return True
  else :
    if a[len(b)*-1:]== b:
      return True
  return False
