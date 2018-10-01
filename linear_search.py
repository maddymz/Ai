# algorithm to search an element 

import random 

# linear earch function 
def linear_search(value, array): 
    for i in range(len(array)):
        while(array[i] == value):
            return i
        # if(array[i] == value):
        #     return i
        # else : 
        #     return None
    return None
    
#intialization and function call 
value = 10
sample_array_list = random.sample(range(11), 6)
index = linear_search(value, sample_array_list)
print("index of value", index)