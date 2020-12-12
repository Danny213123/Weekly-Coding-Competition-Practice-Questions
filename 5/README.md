You have decided to take a road trip with your family, and your family wants to visit an area with n amount of cities.

Each city has an attraction value from 1-10

The road on which these cities are located is oddly linear, which means that they are named after their location on the road.

For example, the road "-20" is located 20 units left from where you will start your road trip. The city "5" is located 5 units to the right of where you will start your road trip.

You can think of this as a number line

--*----------*---------*--------------*-------------*
-10           -3             0                   9                 13

You always start at 0, and you can move either left or right, but you cannot visit the same city more than once.

You also only have a limited amount of fuel, denoted as f, and each one unit of fuel can travel 1 unit on the map (to get to point -3, it takes 3 fuel)

Your goal is to write a program that takes in the number of cities in the area (n), the amount of fuel your car can store (f), and then the cities, along with their attraction value

For example:
5 - number of cities
20 - amount of units you can travel
5 5 - city 5, with an attraction value of 5
8 7 - city 8, with an attraction value of 7
15 10 - city 15, with an attraction value of 10
-3 5 - city -3, with an attraction value of 5
-7 4 - city -7, with an attraction value of 4

Your goal is to find the path you can take that will give you the highest attraction value, for the amount of fuel you have in your car

Sample output:

[5, 8, 15] - this is the path taken (in order), with an attraction value of 22

NOTE: travelling from -2 to -4 is 2 units. Traveling from -2 to 4 is 6 units! Don't forget to include the distance travelled from your start point (0), to your first point.

Test Cases:

INPUT:

      4
      10
      3 7
      -2 5
      1 4
      8 5
      
      OUTPUT:
      [-2, 1, 3]
      
      INPUT:
      3
      9
      5 3
      7 6
      -1 4
      
      OUTPUT:
      [-1, 5, 7]
      
      INPUT:
      5
      30
      5 5
      2 3
      -2 5
      -10 10
      7 10
      
      OUTPUT:
      [-10, -2, 2, 5, 7]
      
      INPUT:
      6
      12
      4 2
      1 8
      -1 7
      -7 10
      10 8
      2 3
      
      OUTPUT:
      [-1, 1, 2, 4, 10]
      
      INPUT:
      7
      25
      8 8
      13 4
      -3 7
      -4 1
      -13 8
      20 9
      2 1
      
      OUTPUT:
      [2, 8, 13, 20]
