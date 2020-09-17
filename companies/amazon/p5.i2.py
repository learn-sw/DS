#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'cutFilms' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputList as parameter.
#

def cutFilms(inputList):
    # Write your code here
    
    # len_input_list: lenght of inputList
    m, len_input_list = {}, len(inputList)
    
    # m: dictinary to store index of character last occurances
    for index in range(len_input_list):
        m[inputList[index]] = index
    
    result = []
    
    left, right = 0,0
    
    # iterate thru th einputy list
    # if right pointer matches the index then it's a scene,  \
    # after match adjust the left pointer

    # length of the scene equals to  right-left+1, append to the result
    for index in range(len_input_list):
        right = max(right, m[inputList[index]])
        if right == index:
            result.append(right-left+1)
            left = right +1
    return result


if __name__ == '__main__':