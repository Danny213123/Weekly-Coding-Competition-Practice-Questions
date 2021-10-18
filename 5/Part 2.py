from itertools import permutations

# returns all 'x' within the dictionary data structure
def getDistance(dict):
  return dict['x']

# returns all 'y' within the dictionary data structure
def getAttraction(dict):
  return dict['y']


# Function takes the main list which contains the cities locations and their respective attraction values
# with the total fuel and current index. The function will run through the current index and returns a score.
def planTrip(main_list, total_fuel, current_index):
    
    plan = {};
    
    areas = []
    
    current_position, score = 0, 0
    
    # Runs through the current index
    for x in current_index:
        
        # Checks to see if the car is able to go to the position and not have negative fuel
        if (total_fuel - abs((current_position) - (main_list[x]['x'])) >= 0):
            
            # The total fuel will decrease by the current position minus the next position
            total_fuel -= abs((current_position) - (main_list[x]['x']))
            
            # Changes the current position to the new position
            currentPosition = main_list[x]['x']
            
            # The score will increase by the position's attraction value
            score += main_list[x]['y']
            
            # The areas visited will be added to the areas list
            areas.append(currentPosition)
        
        # If moving to the new position will result in a negative fuel, it will break out of the loop
        else:
            break
        
    # The plan dictionary will have the areas and scores added
    plan['x'] = areas
    plan['y'] = score
    return plan

if __name__ == "__main__":
    
    total_cities = int(input("Total number of cities: "))
    
    total_fuel = int(input("Total number of fuel: "))
    
    main_dict = []
     
    for x in range (total_cities):
        
        # Each time the loop runs, the temporary dictionary will reset
        temp_dictionary = {};
          
        # Gets location information from user
        location_input = input("City distance and attraction value: ").split()
          
        # The x value is put into a temporary dictionary data structure
        temp_dictionary['x'] = int(location_input[0])
          
        # The y value is put into a temporary dictionary data structure
        temp_dictionary['y'] = int(location_input[1])
          
        #The temp dictionary is appended into the main list
        main_dict.append(temp_dictionary)
         
    # print(main_dict)
    # Sorts the main_dict, the cities will be sorted by distance
    main_dict.sort(key = getDistance)
         
    indexes = []
    
    # takes the indexes so if there are 5 total cities, the indexes would be 0, 1, 2, 3, 4
    for x in range (total_cities):
        indexes.append(x)
    
    # Takes all the possible permutations of the indexes
    all_possible_indexes = permutations(indexes)
         
    score = []
    
    # For all possible index permutations, check the current index's total score
    for current_index in all_possible_indexes:
        score.append(planTrip(main_dict, total_fuel, current_index))
    
    # Sorts all the score index using the key getAttraction.
    # So the score list of indexes of dicts with 'x' and 'y',
    score.sort(key = getAttraction)
    print(f"The cities at {score[-1]['x']} will give you the most score of '{score[-1]['y']}'")
