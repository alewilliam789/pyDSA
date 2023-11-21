def insertionsort(array):


    for i,x in enumerate(array):
        j = i-1
        while(j >=0):
            current_value = array[j+1]
            if(array[j] > current_value):
                array[j+1] = array[j]
                array[j] = current_value
            j -= 1



    return array

