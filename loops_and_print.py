def enumerate_list(colors):
    result = []
    for index, color in enumerate(colors):
        if color: 
            result.append(f"{len(result)}. {color}")  
    return result

def enumerate_backwards(colors):
    result = []
    for index, color in enumerate(colors):
        if color:  
            result.append(f"{len(result)}. {color[::-1]}")  
    return result


colors = ["Red", "Green", "", "White", "Black"]

print(enumerate_list(colors))
print(enumerate_backwards(colors))
