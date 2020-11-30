Spam = ["800", "909"]
PN = str(input())

for x in range (len(Spam)):
  if (PN[len(PN) - 3:] == Spam[0]):
    print("Spam")

print(PN[4], PN[4:5], PN[5:6])

if (PN[4] == PN[4:5] and PN[4:5] == PN[5:6]):
  print("Spam")

if (len(PN) > 4):
  if (PN[len(PN) - 4] == PN[len(PN)] and PN[len(PN) - 3] == PN[len(PN) - 2]):
    print("Spam")
