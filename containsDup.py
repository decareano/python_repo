def containsDup(s):
    n = len(s)  #variable n
    
    #for loop construct
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                return True
            print(s[i])
            print(s[j])
        return False
    
        
containsDup([1,2,3,1])
