def p(n):
  for x in range (2, n - 1):
    if (n % x == 0):
      return False
  return True
 
def f(n):
  if (n == 1):
    return n
  elif (p(n) == False):
    return n * f(n - 1)
  else:
    return f(n - 1)
 
k = f(int(input()))
#print(k)
