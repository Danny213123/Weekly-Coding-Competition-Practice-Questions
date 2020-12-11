import datetime
 
day, month, year = 1, 1, 1901
 
sundays = 0
 
for x in range (year, year + 100):
  for y in range (1, 13):
    ans = datetime.date(x, y, day)
    if (ans.strftime("%A") == "Sunday"):
      sundays += 1
print(sundays)

# With out using datetime module: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
