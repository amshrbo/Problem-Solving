### Problem info
- website: HackeRank
- Name: sparse arrays
- Difcullty: Medium

### Probelm describiton summary
- Describtion:
    - Given two arrays (strings, queries) return how many times every string in the array queries appears in array strings.
    - e.g, `strings = ['hello', 'how', 'are', 'are', 'how']` `queries = ['are', 'you', 'how']`, the output should be like `2 0 2` 

- Input: 
    - `strings` as the array of strings 
    - `queries` the array that I will check it for how many times it appears in strings. 

### My solution
- I simply tackled the problem by thinking about looping over the queries arry and take every query and check for it in the whole strings array this problem will be `Big O(s*q)`.
    > As s the len of the strings array and q is the length of the quries array.
    - I've implemented this solution using two different ways the first with two loops in the file [mysolution](./mysolution.py).
    - And the second with one line of code using list comprehension and `str.count()` function in the [onelineSolution file](./onelineSolution.py) 

### The best solution
- It's built on the same idea but using different data structure **Hash Maps (Dictionaries)** in [best solution](./bestsolution.py) file
    - Dict has a constant time look ups instead of linear time
    - First defining a dictionary using string with queries as the keys and  zeros as the values.
    - loop over the strings array and look for every key in the array and increment by one if exist.
    return the count.

### Notes
- Simply look at the best solution.
    - Defining dict from a string with one default value as zero
- Also In onelineSolution file look for the online implementation.