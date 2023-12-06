def twoWayMerge(lst1, lst2):
    
    i = 0;
    j = 0;
    end1 = len(lst1)-1;
    end2 = len(lst2)-1;
    mergedList = [];
    
    
    while(i <= end1 or j <= end2):
        if(i <= end1 and j <= end2):
            if(lst1[i] >= lst2[j]):
                mergedList.append(lst2[j]);
                j += 1;
            else: 
                mergedList.append(lst1[i])
                i += 1;

        elif( i <= end1):
            mergedList.append(lst1[i]);
            i += 1;
        else:
            mergedList.append(lst2[j]);
            j += 1;

    return mergedList;



            
        
          
