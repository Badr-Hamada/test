


def find_pair(X,Sum):
    
    result = []
    
    n = len(X)
    
    for i in range(0,n-1):
        for j in range(i+1 ,n) : 
            if X[i] + X[j] == Sum : 
                result.append((X[i],X[j]))
    return result




# run 

x=[1,2,3,4,5,6,7]

sum = 9

print(find_pair(x,sum))

    