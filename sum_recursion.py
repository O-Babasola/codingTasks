
#Base case: if index is 0, then return the first element of the list
#This is the stopping condition for the recursion.
#Recursive case: the function calls itself, but with the index being reduced by one
#This step moves the recursion towards the base case
#It also adds the current indexed value to the result of the recursion
#This accumulates the sum as the recursion unfolds back towards the first call
#Update the maximum value if the current number is less than max_val
#Base case: if the index is equal to the length of the list, 
#returns the maximum value found.
def adding_up_to(arr, index):
    if index == 0:
        return arr[0]
    else:
        return  arr[0] + adding_up_to(arr, index - 1)
        
#prints results of recursion
print(adding_up_to([1,2,3,4,5], 2))