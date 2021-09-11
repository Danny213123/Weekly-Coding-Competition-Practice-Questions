input_storage = []
grid = []

# If you want to visualize the graph, you can un-comment the get_grid() function in the main loop
# Github: https://github.com/Danny213123/CCC-Practice/blob/main/CCC%20'05%20J4.py

# How it works:
# It runs an operation until it hits a wall, then it switches operations
# operation 1: move right, move down, move right, goto operation 2
# operation 2: move left, move down, move left, goto operation 3
# operation 3: move up, move left, move up, goto operation 4
# operation 4: move right, move up, goto operation 0

def get_grid():
  #print("=" * len(grid[0]))
  for x in range (len(grid)):
    print(grid[x])

for x in range (5):
  input_storage.append(int(input()))

currentx, currenty, = input_storage[2] + 1, 1

temp_temp_grid = ["#"] * (input_storage[0] + 2)
grid.append(temp_temp_grid)
# Initialize grid
for i in range (input_storage[1]):
  temp_grid = [""] * (input_storage[0] + 2)
  for j in range (input_storage[0] + 2):
    temp_grid[j] = "."
  grid.append(temp_grid)
grid.append(temp_temp_grid)

# Set up top blocked area
for x in range (1, input_storage[3] + 1):
  for y in range (1, input_storage[2] + 1):
    grid[x][y] = "#"
    grid[x][len(grid[0]) - y - 1] = "#"

# Set up bottom blocked area
for x in range (len(grid) - input_storage[3] - 1, len(grid) - 1):
  for y in range (1, input_storage[2] + 1):
    grid[x][y] = "#"
    grid[x][len(grid[0]) - y - 1] = "#"

for x in range (len(grid)):
  grid[x][0], grid[x][len(grid[x]) - 1] = "#", "#"

total_moved = 0
operation = 0

grid[currenty][currentx] = "M"
broken = 0

while (total_moved != input_storage[4]):
  past_x, past_y = currentx, currenty
  get_grid()
  if (operation == 0):
    if (grid[currenty][currentx + 1] != "#" and grid[currenty - 1][currentx] == "#"):
      grid[currenty][currentx] = "#"
      total_moved+= 1
      broken = 0
      currentx += 1
      grid[currenty][currentx] = "M"
    elif (grid[currenty][currentx + 1] == "#" and grid[currenty + 1][currentx] != "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currenty += 1
      grid[currenty][currentx] = "M"
    else:
      broken += 1
      operation = 1
  if (operation == 1):
    if (grid[currenty][currentx - 1] != "#" and grid[currenty + 1][currentx] == "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currentx -= 1
      grid[currenty][currentx] = "M"
    elif (grid[currenty][currentx + 1] == "#" and grid[currenty + 1][currentx] != "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currenty += 1
      grid[currenty][currentx] = "M"
    else:
      broken += 1
      operation = 2
  if (operation == 2):
    if (grid[currenty][currentx - 1] == "#" and grid[currenty - 1][currentx] != "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currenty -= 1
      grid[currenty][currentx] = "M"
    elif (grid[currenty][currentx - 1] != "#" and grid[currenty + 1][currentx] == "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currentx -= 1
      grid[currenty][currentx] = "M"
    else:
      broken += 1
      operation = 3
  if (operation == 3):
    if (grid[currenty][currentx + 1] != "#" and grid[currenty - 1][currentx] == "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currentx += 1
      grid[currenty][currentx] = "M"
    elif (grid[currenty - 1][currentx] != "#" and grid[currenty][currentx - 1] == "#"):
      grid[currenty][currentx] = "#"
      total_moved += 1
      broken = 0
      currenty -= 1
      grid[currenty][currentx] = "M"
    else:
      broken += 1
      operation = 0
  if (broken > 4):
    break
    

grid[currenty][currentx] = "M"
print(currentx)
print(currenty)
#get_grid()
