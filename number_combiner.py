'''
This code works by having each number in the list have zero padding at the end of the digit
based on its position on the list.

For example, [1, 2, 3, 4] hs 4 digits, so we want to make the first number have 4 digits using
0 padding, the second have 3 digits, the third have 2 digit and last have 1.

Thus, we get [1000, 200, 30, 4] then we add them together to get 1234
'''

def number_combiner(lst: list) -> int:
    '''
    takes in a list of integers and combines it

    arg:
    lst(list): a list of integers

    return:
    the combined integer of all digits from lst
    '''

    # initiate counter variable
    n = 0
    # initiate an empty list
    new_list = []

    # for each number in the list
    for num in lst:
        # calculates the power of 10 based on the position of num in the list
        power = len(lst) - 1 - n
        # num times 10 to the power of variable 'power' to get num with appropriate 0 padding
        # resulting number is appended to a new list
        new_list.append(num * 10 ** power)
        # increase counter by one
        n += 1

    # return the result as a sum of all the integers in the list we appended all the integers to
    return sum(new_list)


# input a list of numbers
num_list = [8, 3, 5, 1]

# prints result of the function
print(number_combiner(num_list))






