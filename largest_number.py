#returns the largest number in a list of integers taken as an argument

#defines a code named "find_minimum"
#Update the maximum value if current curent is less than max_val
#Recursive case: function calls itself with the next index and the current maxmimum
def find_maximum(numbers, index = 0, max_val=float("-inf")):
    if index == len(numbers):
        return max_val
    current_max = max(max_val, numbers[index])

    return find_maximum(numbers, index + 1, current_max)


print(find_maximum([1,2,3,7,5,100]))