def merge(array,start,mid,end):

    if(start > mid or mid > end):
        return

    i = start
    j = mid+1
    sorted_array = []

    while(i <= mid or j <= end):
        if(i <= mid and j <= end):
            if(array[i] <= array[j]):
                sorted_array.append(array[i])
                i += 1
            else:
                sorted_array.append(array[j])
                j += 1
        elif(i <= mid):
            sorted_array.append(array[i])
            i += 1
        else:
            sorted_array.append(array[j])
            j += 1
    
    for k in range(start,end+1):
        array[k] = sorted_array[k-start]



def mergesorter(array,start,end):


    if(start >= end):
        return
    elif(start+1 == end):
        if(array[start] > array[end]):
            array[start],array[end] = array[end], array[start]
    else:
        mid = (end+start)//2
        mergesorter(array,start,mid)
        mergesorter(array,mid+1,end)
        merge(array,start,mid,end)


def mergesort(array):

    if(len(array) <= 1):
        return
    else:
        mergesorter(array, 0, len(array)-1)







