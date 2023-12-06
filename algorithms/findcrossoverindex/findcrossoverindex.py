def findCrossoverIndexHelper(x, y, left, right):
    
    if(left+1 == right):

        if(left > 0):
            if(float(x[left-1]) >= float(y[left-1]) and float(x[left]) < float(y[left])):
                return (left-1)
        
        if((float(x[left]) >= float(y[left])) and float(y[right]) > float(x[right])):
                return left
    else:
        mid = (right+left)//2;
        leftValue = findCrossoverIndexHelper(x,y,left,mid);
        rightValue = findCrossoverIndexHelper(x,y,mid+1,right);
        
        if(leftValue != None and leftValue < len(x)-1):
            return leftValue;
        elif(rightValue != None and rightValue < len(x)-1):
            return rightValue;
        else:
            return len(x)-1


def findCrossoverIndex(x, y):
    n = len(x)
    if(n <= 1):
        return 0
    else:
        return findCrossoverIndexHelper(x, y, 0, n-1);




