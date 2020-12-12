from itertools import permutations
 
Cities = int(input())
Fuel = int(input())
h = []
 
for x in range (Cities):
  q = {};
  c = input().split()
  q['x'] = int(c[0])
  q['y'] = int(c[1])
  h.append(q)
print("done")
 
def getDistance(dict):
  return dict['x']
 
def getAttraction(dict):
  return dict['y']
 
h.sort(key = getDistance)
 
s = []
 
for x in range (Cities):
  s.append(x)
 
z = permutations(s)
 
def planTrip(s, Fuel, c):
  plan = {};
  areas = []
  currentPosition, score = 0, 0
  for q in c:
    if (Fuel - abs((currentPosition) - (s[q]['x'])) >= 0):
      Fuel -= abs((currentPosition) - (s[q]['x']))
      currentPosition = s[q]['x']
      score += s[q]['y']
      areas.append(currentPosition)
    else:
      break
  plan['x'] = areas
  plan['y'] = score
  return plan
 
score = []
for l in z:
  print (l)
  score.append(planTrip(h, Fuel, l))
 
score.sort(key = getAttraction)
print(score[-1])
