# Implementation of the rotateLeft function
def rotateLeft(d, arr):
    for i in range(d):
        # getting the first element of the array
        first = arr[0]

        # Creating a temp array
        rotLeft = []
        for i in range(len(arr)):
            if i == (len(arr) - 1):
                break
            else:
                # append every element in the arr to rotleft but in idx - 1
                rotLeft.append(arr[i + 1])
                
        # append the arr[0] to the end of rotLeft
        rotLeft.append(first)
        arr = rotLeft
    return arr