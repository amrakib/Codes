#Task 01: Merge Lineup
import fhm_unittest as unittest
import numpy as np
def mergeLineup(pokemon_1, pokemon_2):
    i = 0
    j = len(pokemon_2) - 1
    arr = np.ones(5, dtype=int)
    print(arr)
    while i < len(pokemon_1):
        try:
            arr[i] = pokemon_1[i] + pokemon_2[j]
        except:
            if pokemon_1[i] == None:
                arr[i] = pokemon_2[j]
            elif pokemon_2[j] == None:
                arr[i] = pokemon_1[i]
        i += 1
        j -= 1
    return arr

print("///  Task 01: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None] )
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [12, 3, 28, -8, 5]
unittest.output_test(returned_value, np.array([12, 3, 28, -8, 5]))
pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [4,17,6,27,2]
unittest.output_test(returned_value, np.array([4,17,6,27,2]))