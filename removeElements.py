def removeElement(elems, target):
    index = 0
    
    for i in range(len(elems)):
        if elems[i] != target:
            #elems[i] to elems[index] that is zero
            elems[index] = elems[i]
            print(elems[index])
            print(index, elems[index])
            index += 1
        
        
    return index          
removeElement([2,4,7,9,2,0,1,10,12,2], 2)
