def bubblesort(array):


    for element in range(len(array)-1):

        for i,x in enumerate(array):
            if(i > 0):
                if(array[i-1] > x):
                    array[i] = array[i-1]
                    array[i-1] = x
            print(array)


    return array

