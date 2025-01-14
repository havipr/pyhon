from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print a list that contains exactly the same numbers as the given list,    //
## but rearranged so that every 3 is immediately followed by a 4. Do not     //
## move the 3's, but every other number may move. The list contains the      //
## same number of 3's and 4's, every 3 has a number after it that is not a 3 //
## or 4, and a 3 appears in the list before any 4.                           //
##    1, 3, 1, 4  -> 1, 3, 4, 1                                              //
##    1, 3, 1, 4, 4, 3, 1  -> 1, 3, 4, 1, 1, 3, 4                            //
##    3, 2, 2, 4  -> 3, 4, 2, 2                                              //
##/////////////////////////////////////////////////////////////////////////////

def fix_34(nums):
    threes = [i for i in range(len(nums)) if nums[i] == 3]
    fours = [i for i in range(len(nums)) if nums[i] == 4]
    
    new_nums = nums[:]
    for i in range(len(threes)):
        new_nums[fours[i]] = new_nums[threes[i]+1]
        new_nums[threes[i]+1] = 4
    
    return new_nums
