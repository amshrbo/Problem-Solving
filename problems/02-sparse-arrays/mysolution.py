# A simple problem with a simple solution 
def matchingStrings(strings, queries):
    counts = []
    
    for i in range(len(queries)):
        counter = 0

        for j in range(len(strings)):
           if queries[i] == strings[j]:
                counter = counter + 1
                
        counts.append(counter)
    
    return counts