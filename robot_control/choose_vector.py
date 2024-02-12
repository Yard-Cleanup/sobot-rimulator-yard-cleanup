import random
import copy 
arr = ['Start'] #Default value
directions = ['North', 'North-East', 'East', 'South-East', 'South', 'South-West', 'West', 'North-West']

def choose_vector():
    directions_new = copy.deepcopy(directions)

    if arr[0] == 'Start':
        arr[0] = random.choice(directions)
        return arr[0]
    
    opposite_index = ( (directions_new.index(arr[0]) +4 ) % len(directions))
    directions_new.remove(opposite_index)
    print("Directions", directions)
    print("Directions_new", directions_new )
    arr[0] = random.choice(directions)
    return arr[0]


chosen_vector = choose_vector()
print("Random vector:", chosen_vector)

chosen_vector = choose_vector()
print("Random vector:", chosen_vector)