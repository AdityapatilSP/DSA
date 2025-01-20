#Question : You are given an array of Integers in which each subsequent value is not less than the previous value.
#Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order


def sorted_squared(array):

    n = len(array)
    res = [0]*n
    for i in range(n):
        res[i] = array[i]**2
    res.sort()
    return res

print(sorted_squared([1, 2, 3, 4, 5]))
