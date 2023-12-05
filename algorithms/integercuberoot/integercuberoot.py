import math


def integerCubeRootHelper(n, left, right):
    mid = (right+left)//2;
    value = mid*mid*mid;

    while( mid >= left and mid <= right):

        if(value == n):
            return mid;
        elif(value < n):
            mid = (right+mid+1)//2;
            value = mid*mid*mid;
        else:
            while( mid >= left):
                if(value <= n):
                    return mid;

                mid -= 1
                value = mid*mid*mid










def integerCubeRoot(n):
    if(n == 1):
        return 1;
    else:
        return integerCubeRootHelper(n, 0, math.ceil(math.sqrt(n)))

