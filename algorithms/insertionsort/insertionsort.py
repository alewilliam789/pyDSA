def insertionsort(array):


    for i in range(len(array)):
        j = i-1
        while(j >=0):
            current_value = array[j+1]
            if(array[j] > current_value):
                array[j+1] = array[j]
                array[j] = current_value
            else:
                break
            j -= 1



    return array

