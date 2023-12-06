def integerCubeRootHelper(n, left, right):
    cube = lambda x: x*x*x; # anonymous function to cube a number
    
    assert(n >= 1)
    assert(left < right)
    assert(cube(left) < n)
    assert(cube(right) > n)
    
    if(left < right):
        if(left+1 == right):
            leftValue = cube(left);
            rightValue = cube(right);
            if(leftValue <= n or rightValue <=n):
                if(rightValue <= n):
                    return right;
                else:
                    return left;
    
        else:
            mid = (right+left)//2;
            value = cube(mid);
            if(value > n):
                return integerCubeRootHelper(n,left,mid)
            elif(value < n):
                return integerCubeRootHelper(n,mid,right)
            else:
                return mid


def integerCubeRoot(n):
    if(n == 1):
        return 1;
    else:
        return integerCubeRootHelper(n, 0, n-1)

