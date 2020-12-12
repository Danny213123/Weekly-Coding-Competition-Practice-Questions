a, b, z = input().split()

def time(a, b):
  if (a == 0): return a
  return ((a) + time(a - b, b))

d, c = (1200 / int(z)) * ((int(a) / int(b)) + 1), (time(int(a), int(b)) * 2)
print(d + c)
