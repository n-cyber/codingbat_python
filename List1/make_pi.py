
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


# make_pi() → [3, 1, 4]

def make_pi():
  pi='3.14'
  res = []
  for i in range(len(pi)):
    if pi[i] in ['0','1','2','3','4','5','6','7','8','9']:
      res.append(int(pi[i]))
  return res

