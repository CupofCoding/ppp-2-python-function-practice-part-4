# Acceptance Criteria
# Each of the functions described exists in the Python file.
# Each of the functions is named correctly, accepts the correct parameters, returns the correct output, and has been called inside the file (so that each function runs automatically when the file is run).
# The file runs with no errors.

# Write a Python function called max_num()to find the maximum of three numbers.
def max_num( a,b,c ):
    return max([a,b,c])

print(max_num(1,2,3))
print(max_num(15,100,50))
print(max_num(15,20,5))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list (list):
    if (len(list) == 0): return 0
    
    product = list[0]

    if len(list) > 1:
        for i in list[1:]:
            product = product * i
        
    return product

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([60]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

print(rev_string(""))
print(rev_string("apple"))
print(rev_string("mt string"))

# Write a Python function called num_within() to check whether a number falls in a given range.
## The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
## Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(mid, low, high):
    if (low > high):
        return "2nd argument MUST be less than 3rd arg"
    return (low <= mid and mid <= high)

print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
## The function accepts the number n, the number of rows to print
## Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

# Firstly, an input number is taken from the user to define the number of rows.
integer = int(input("Enter the number of rows: "))

# Secondly, an empty list is defined, which is used to store values.
list = [] #an empty list

# Then, a for loop is used to iterate from 0 to n-1 that append the sub-lists to the initial list.
def pascal():
    for n in range(integer):
        list.append([])
    
# After that, 1 is appended to the list.
    if(integer != 0):
        list[n].append(1)

# Then, a for loop is used again to put the values of the number inside the adjacent row of the triangle.
    for m in range(1, n):
        list[n].append(list[n - 1][m - 1] + list[n - 1][m])
    if(integer != 0):
        list[n].append(1)
# Finally, the Pascal Triangle is printed according to the given format.
    for n in range(integer):
        print(" " * (integer - n), end = " ", sep = " ")
        for m in range(0, n + 1):
            print('{0:5}'.format(list[n][m]), end = " ", sep = " ")
        print()

# def pascal():
# 	#your code here

#     pascal(1)
#     '''
# output:
# 1
# '''

# pascal(5)
# '''
# output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# '''