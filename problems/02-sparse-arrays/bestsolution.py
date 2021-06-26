# using dict as it's better in lookups
def matchingStrings(strings, queries):
    # Initializing a dictionary from the strings with 0 as default values 
    qs_dict = dict.fromkeys(queries, 0)

    for value in strings:
        if value in qs_dict:
            qs_dict[value] += 1

    # looping over q to get the order back 
    return [qs_dict[q] for q in queries]