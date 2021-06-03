#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER flightDuration
#  2. INTEGER_ARRAY movieDuration
#

def foo(flightDuration, movieDuration):
    target_movies_duration = flightDuration - 30
    movies_duration = {}

    for index in range(len(movieDuration)):
        diff = target_movies_duration - movieDuration[index]

        if diff in movies_duration:
            return [movies_duration[diff],index]
        else:
            movies_duration[diff] = index






def foo(flightDuration, movieDuration):
    # Write your code here
    if not flightDuration or not movieDuration or flightDuration<30:
        return []
    
    target_movies_duration = flightDuration - 30
    movies_duration = {}

    for index in range(len(movieDuration)):
        if movieDuration[index] not in movies_duration:
            movies_duration[movieDuration[index]] = index
    
   
    i, j = 0, 0
    left, right = 0, len(movieDuration)-1
    # this will keep the info of the longest movie 
    
    max_val = -1
    # sorted movie durations
    sorted_movies = sorted(movieDuration)
    # print(sorted_movie_duration)
    
    while left < right:
        
        # check if 2 movie durations are less than equal to the targeted_duration
        if sorted_movies[left] + sorted_movies[right] <= target_movies_duration:
            if max_val < sorted_movies[left] + sorted_movies[right]:
                max_val = sorted_movies[left] + sorted_movies[right]

                i , j = movies_duration[sorted_movies[left]] , movies_duration[sorted_movies[right]]


            left+=1
        # if movie duration exceeds targeted time than move the right pointer
        # As the movie durations are in sorted order, compare left and right-1
        else:
            right -=1
    

    return(sorted([i,j]))

if __name__ == '__main__':

m_d = [250, 5, 100, 180, 40, 120, 10]
