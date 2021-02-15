from time import *
from quicksort import *
from merge_sort import *

"""
Fonctions de tri
"""
def selection_sort(sequence):
    for i in range(0, len(sequence)-1) :
        smallest_index = i
        for j in range(i+1, len(sequence)) :
            if sequence[j] < sequence[smallest_index] :
                smallest_index = j
        if smallest_index != i :
            smallest_value = sequence[smallest_index]
            sequence[smallest_index] = sequence[i]
            sequence[i] = smallest_value
    return sequence


def insertion_sort(sequence):
    for i in range(1, len(sequence)) :
        insert_value = sequence[i]
        j = i
        while j > 0 and sequence[j-1] > insert_value :
            sequence[j] = sequence[j-1]
            j = j-1
        sequence[j] = insert_value    
    return sequence




"""
SÃ©quences de test
"""
word_sequence = ['black', 'end', 'end', 'end', 'hello', 'moon', 'sun', 'up', 'up', 'white', 'alpha', 'black', 'black', 'down', 'down', 'down', 'end', 'hello', 'moon', 'omega', 'alpha', 'down', 'down', 'down', 'end', 'hello', 'moon', 'sun', 'white', 'white', 'begin', 'down', 'down', 'end', 'moon', 'omega', 'omega', 'up', 'up', 'up', 'alpha', 'alpha', 'begin', 'down', 'end', 'end', 'moon', 'moon', 'up', 'white']
tuple_sequence = [(12, -105, -20), (-28, -67, -82), (26, 122, -122), (-47, -96, -56), (46, -92, -120), (-102, 55, 100), (-57, -88, -15), (-19, -89, -59), (-92, -41, -101), (69, -49, -12), (84, 29, 43), (32, 95, -105), (-69, 92, 106), (20, 8, 14), (-57, 69, -23), (87, 89, -124), (93, 35, -67), (26, 59, -49), (3, -49, 91), (-59, 21, -75), (-73, 20, 27), (30, -21, 124), (-112, 78, -54), (-74, 105, 9), (-27, -69, 64), (69, 115, -87), (125, 110, -4), (117, -107, 81), (81, -61, 87), (70, -83, -40), (-92, 29, 126), (48, 118, 104), (86, 39, 112), (119, 26, 67), (-23, 30, 101), (76, -118, 119), (-103, 46, -67), (-6, -94, 52), (17, -61, 7), (-51, 3, 32), (50, -75, 52), (-76, -28, -45), (35, 74, 28), (-41, -96, -32), (-19, 89, -64), (-86, -42, -22), (-32, 50, 86), (94, -38, -97), (10, -118, -58), (-26, -14, 20)]
int_sequence = [-37, -19, -4, -12, -44, -92, 8, -106, -65, 64, -99, -107, -119, -24, -106, 38, 86, -78, 56, 24, -49, -32, 18, 86, 101, 11, 120, -124, 39, -38, -49, -55, 5, 90, -42, 60, -9, 62, -113, -124, -79, -112, 66, -32, -30, 59, -42, -29, -44, 114]
float_sequence = [3.79, 6.69, 6.74, 0.23, 2.55, 4.95, 1.84, 7.98, 1.65, 2.42, 5.7, 1.23, 3.91, 8.39, 4.91, 9.09, 7.73, 3.06, 3.91, 8.81, 9.41, 9.6, 6.5, 3.13, 0.81, 0.74, 7.66, 9.63, 3.16, 5.44, 6.31, 7.66, 7.08, 4.68, 0.82, 1.66, 5.34, 0.63, 4.96, 4.76, 3.32, 9.07, 7.31, 6.96, 1.27, 3.61, 2.79, 8.1, 2.74, 3.45]
bool_sequence = [False, False, True, True, True, False, False, True, True, True, False, True, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, True, False, True, False, False, False, True, True, False, True, True, True]
int_1000_sequence = [1, 5, 3, 5, 5, 2, 6, 0, 7, 8, 8, 3, 2, 0, 5, 7, 3, 6, 9, 5, 6, 0, 5, 2, 6, 6, 8, 0, 3, 9, 1, 4, 1, 6, 1, 6, 7, 1, 8, 1, 2, 8, 9, 8, 6, 7, 7, 9, 2, 7, 4, 3, 9, 1, 5, 1, 2, 4, 6, 5, 2, 2, 7, 3, 0, 3, 8, 7, 4, 6, 9, 4, 4, 4, 4, 2, 5, 1, 1, 4, 1, 3, 5, 5, 4, 6, 4, 2, 3, 9, 5, 8, 8, 7, 8, 0, 6, 9, 9, 2, 6, 5, 6, 1, 7, 0, 0, 5, 0, 5, 1, 7, 6, 9, 8, 4, 7, 9, 1, 3, 6, 1, 9, 2, 9, 1, 4, 4, 6, 7, 2, 1, 2, 7, 0, 9, 6, 0, 0, 5, 0, 4, 4, 4, 2, 9, 7, 2, 9, 5, 3, 6, 1, 0, 8, 2, 3, 4, 8, 9, 4, 3, 8, 9, 0, 2, 5, 6, 0, 2, 2, 0, 8, 3, 9, 9, 4, 4, 0, 6, 0, 8, 4, 2, 4, 6, 2, 2, 4, 5, 5, 3, 9, 0, 7, 8, 6, 0, 5, 3, 1, 8, 3, 1, 6, 5, 9, 2, 0, 6, 5, 3, 1, 5, 4, 8, 2, 9, 8, 2, 6, 2, 1, 2, 9, 5, 0, 4, 3, 6, 4, 1, 7, 7, 9, 7, 6, 1, 9, 9, 0, 9, 1, 2, 9, 2, 6, 9, 0, 2, 9, 4, 8, 8, 9, 4, 9, 2, 9, 9, 0, 1, 1, 6, 3, 3, 5, 0, 9, 7, 8, 4, 3, 8, 8, 5, 5, 9, 2, 1, 7, 5, 8, 0, 9, 5, 2, 7, 4, 7, 0, 6, 9, 5, 6, 3, 9, 5, 2, 1, 9, 6, 6, 8, 5, 7, 4, 1, 0, 1, 7, 2, 0, 0, 2, 8, 5, 8, 4, 3, 3, 3, 4, 6, 8, 6, 6, 9, 7, 0, 0, 9, 8, 0, 5, 6, 8, 5, 2, 5, 9, 5, 6, 7, 5, 8, 3, 1, 9, 8, 8, 2, 1, 3, 0, 0, 5, 3, 3, 7, 2, 4, 5, 9, 0, 1, 2, 2, 2, 5, 3, 0, 9, 6, 8, 2, 2, 6, 8, 4, 7, 6, 5, 1, 6, 0, 9, 2, 8, 0, 1, 5, 7, 4, 5, 5, 5, 5, 5, 6, 1, 4, 4, 3, 6, 5, 5, 8, 0, 9, 9, 9, 8, 2, 8, 2, 4, 6, 1, 5, 3, 1, 1, 9, 4, 6, 0, 1, 8, 3, 6, 9, 8, 7, 8, 7, 6, 9, 6, 7, 0, 1, 2, 1, 5, 8, 1, 6, 1, 6, 7, 3, 1, 7, 7, 7, 9, 2, 8, 7, 4, 0, 0, 2, 7, 9, 3, 3, 8, 1, 3, 1, 2, 9, 5, 7, 1, 7, 9, 7, 2, 4, 2, 3, 9, 2, 9, 7, 5, 6, 6, 8, 2, 9, 4, 1, 4, 3, 8, 5, 6, 1, 9, 0, 6, 0, 9, 6, 9, 7, 7, 1, 8, 1, 7, 8, 3, 5, 1, 9, 9, 5, 2, 1, 1, 9, 3, 6, 0, 3, 0, 9, 8, 1, 9, 1, 2, 7, 5, 9, 9, 7, 3, 8, 9, 8, 7, 7, 6, 4, 2, 0, 2, 9, 7, 2, 0, 4, 2, 2, 2, 6, 2, 7, 8, 9, 4, 9, 7, 1, 9, 4, 3, 4, 4, 3, 3, 0, 3, 0, 3, 8, 5, 4, 4, 3, 5, 0, 8, 2, 7, 4, 1, 3, 3, 0, 3, 8, 3, 9, 4, 1, 6, 8, 7, 4, 5, 9, 0, 5, 0, 5, 6, 6, 0, 2, 5, 8, 0, 0, 8, 0, 6, 6, 8, 6, 8, 1, 8, 4, 3, 6, 3, 8, 5, 1, 1, 7, 4, 7, 6, 9, 3, 6, 5, 2, 4, 1, 0, 5, 0, 4, 6, 3, 2, 0, 7, 3, 5, 6, 0, 0, 3, 3, 9, 8, 6, 3, 0, 0, 7, 2, 5, 7, 1, 8, 1, 0, 3, 9, 7, 4, 9, 9, 2, 8, 1, 2, 2, 4, 6, 8, 1, 5, 8, 4, 7, 3, 4, 2, 2, 5, 5, 2, 9, 6, 1, 5, 2, 4, 2, 4, 3, 6, 7, 1, 4, 5, 6, 9, 3, 0, 1, 4, 3, 8, 0, 6, 6, 4, 3, 5, 9, 8, 4, 7, 2, 3, 6, 4, 3, 3, 9, 4, 2, 0, 2, 6, 3, 0, 6, 0, 9, 1, 2, 4, 9, 5, 8, 2, 3, 4, 9, 1, 8, 5, 7, 9, 1, 1, 9, 7, 5, 5, 1, 4, 6, 2, 0, 9, 9, 7, 5, 3, 1, 4, 3, 9, 7, 2, 8, 0, 8, 5, 0, 4, 9, 5, 9, 1, 6, 8, 7, 0, 9, 0, 7, 8, 2, 5, 6, 1, 2, 8, 1, 0, 2, 2, 8, 5, 5, 1, 5, 2, 5, 6, 3, 8, 2, 1, 8, 8, 9, 2, 7, 6, 2, 1, 3, 0, 8, 1, 4, 6, 1, 9, 2, 4, 9, 1, 6, 0, 1, 2, 1, 7, 6, 4, 8, 7, 8, 8, 7, 9, 0, 1, 0, 2, 9, 9, 4, 4, 2, 5, 0, 8, 3, 6, 5, 2, 8, 9, 0, 5, 3, 8, 2, 5, 5, 8, 3, 4, 4, 9, 9, 6, 6, 3, 8, 8, 5, 3, 2, 7, 1, 8, 0, 2, 9, 5, 8, 3, 3, 5, 8, 3, 4, 8, 0, 0, 5, 8, 7, 4, 5, 4, 5, 4, 0, 5, 3, 6, 5, 2, 6, 6, 9, 8, 4, 9, 7, 8, 8, 3, 3, 2, 1, 2, 0, 2, 7, 2, 7, 1, 1, 9, 7, 9, 9, 9, 4, 9, 2, 8, 7, 9, 0, 0, 5, 3, 2, 6, 4, 7, 7, 8, 1, 1, 0, 3, 1, 9, 9, 5, 3, 0, 6, 6, 7, 0, 6, 3, 1, 9, 9, 2, 9, 7, 7, 5]


array = int_1000_sequence 

"""
Appel et rapport de la fonction selection_sort
"""
before = time()
for i in range(1, 100) :
    selection_sort(array.copy())
after = time()
duration = after - before
print("DurÃ©e de lâ€™algorithme de tri par sÃ©lection : ",duration,"s")
"""
Appel et rapport de la fonction insertion_sort
"""
before = time()
for i in range(1, 100) :
    insertion_sort(array.copy())
after = time()
duration = after - before
print("DurÃ©e de lâ€™algorithme de tri par insertion : ",duration,"s")

"""
Appel et rapport de la fonction quicksort
"""

before = time()
for i in range(1, 100) :
    quicksort(array.copy(), 0, len(array) - 1)
after = time()
duration = after - before
print("DurÃ©e de lâ€™algorithme de tri par quicksort : ",duration,"s")


"""
Appel et rapport de la fonction merge_sort
"""

before = time()
for i in range(1, 100) :
    merge_sort(array.copy())
after = time()
duration = after - before
print("DurÃ©e de lâ€™algorithme de tri par merge sort : ",duration,"s")