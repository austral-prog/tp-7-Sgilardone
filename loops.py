def index_of(word, list):
    
    for index, list in enumerate(list):
        if list == word:  
            return index  
    return -1 

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of("Black", colors))

print(index_of("Blue", colors))




def index_of_by_index(word, list, index):
   
    if index < 0 or index >= len(list):
        return -1  

   
    for index in range(index, len(list)):
        if list[index] == word:  
            return index  
            
    return -1  

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_by_index("Black", colors, 1))

print(index_of_by_index("Black", colors, 4))

print(index_of_by_index("Green", colors, 2))





def index_of_empty(list):
   
    for index, list in enumerate(list):
        if list == "":  
            return index  
    return -1  


print(index_of_empty(colors))

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors))


def put(word, list):
    for index in range(len(list)):
        if list[index] == "":  
            list[index] = word  
            return index 
    return -1  

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(put("Blue", colors))


colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(put("Blue", colors))


def remove(word, list):
    count = 0  
    
    for index in range(len(list)):
        if list[index] == word:  
            list[index] = ""  
            count += 1 
    return count

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(remove("Black", colors))

print(remove("Blue", colors))
