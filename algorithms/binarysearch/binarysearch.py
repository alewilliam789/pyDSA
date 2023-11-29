from typing import List
import math

def binarysearch(item : int, list : List):
    start = 0;
    end = len(list)-1
    mid = math.floor((end-start)/2)
    
    for x in range(len(list)):
        if(list[mid] == item):
            return tuple([mid, True])
        elif(list[mid] < item):
            start = mid
            mid = math.ceil((end-start)/2)+mid
        else:
            end = mid-1
            mid = math.floor((end - start)/2)
    
    return False

