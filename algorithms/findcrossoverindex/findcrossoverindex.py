def findCrossoverIndexHelper(x, y, left, right, indexArray):
    
    if(left >= right):
        return;
    
    elif(left+1 == right):

        if(left > 0):
            if(float(x[left-1]) >= float(y[left-1]) and float(x[left]) < float(y[left])):
                indexArray.append(left-1)
        
        if((float(x[left]) >= float(y[left])) and float(y[right]) > float(x[right])):
                indexArray.append(left)
    else:
        mid = (right+left)//2;
        findCrossoverIndexHelper(x,y,left,mid, indexArray);
        findCrossoverIndexHelper(x,y,mid+1,right, indexArray);
    


def findCrossoverIndex(x, y):
    n = len(x)
    indexArray = [];
    if(n <= 1):
        return 0
    else:
        findCrossoverIndexHelper(x, y, 0, n-1, indexArray);

    return indexArray[0];




