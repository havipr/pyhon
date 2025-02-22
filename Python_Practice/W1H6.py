from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////
## Given a list of ints, decide which is larger of the first and         //
## last elements in the list, and set all the other elements to be that  //
## that value. Print the changed list.  Implement functions for:         //
##   - reading the list                                                  //
##   - finding the maximum of 2 integers                                 //
##   - setting all elements of a  list  to a single value                //
##   - printing a  list                                                  //
##    1, 2, 3  ->  3, 3, 3                                               //
##    11, 5, 9  ->  11, 11, 11                                           //
##    2, 11, 3  ->  3, 3, 3                                              //
##/////////////////////////////////////////////////////////////////////////


def read_list():
    return list(map(int, input().split()))

def max_of_two(a, b):
    return a if a > b else b

def set_all_to_value(lst, value):
    for i in range(len(lst)):
        lst[i] = value

def print_list(lst):
    print(*lst)

lst = read_list()
if len(lst) > 1:
    max_val = max_of_two(lst[0], lst[-1])
    set_all_to_value(lst[1:-1], max_val)
print_list(lst)
