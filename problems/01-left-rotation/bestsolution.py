def rotateLeft(d, arr):
    for i in range(d):
        # poping the first element in arr out
        first = arr.pop(0)
        # append first to arr 
        arr.append(first)
    return arr