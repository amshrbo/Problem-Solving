### Problem info
- website: HackeRank
- Name: leftRotate
- Difcullty: Easy

### Probelm describiton summary
- Describtion:
    - Given an array perform a left rotation on it d times, the left rotation is simply shifting the array elements to the left one time.
    - e.g, `arr = [1, 2, 3, 4]` after leftRotate should be `arr = [2, 3, 4, 1]` 

- Input: 
    - `d` as the number of rotation that you should perform in the array
    - `arr` the array you should perform the rotations on

### My solution
- I simply tackled the problem by thinking about copying arr to temp, such that arr[i] copied to temp[i-1]
- Then getting the first element of arr and append it to the end of temp
- After that update assign temp to arr.
- Repeat the above d times

### The best solution
- It's pretty intutive, 
    1. simply poping out the first element of arr in temp
    1. append it again to the end of arr
    1. repeat d times 

- So simple ^_^, isn't it.

### Notes
- Simply look at the best solution it has all the tricks.
- Also In mysolution file look In how did I handle the indeces.