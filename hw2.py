def trace(A):
    row=len(A)
    for i in A:
        if len(i)!=row:
            return ('not square matrix')
    trace=0
    i=0
    while i < len(A):
        trace+=A[i][i]
        i+=1
    return(trace)

A=[[1,2,3],[3,4,5],[1,2,3]]
B=[[1,2],[4,5,6]]
C=[[2,3],[4,5]]
print(trace([[2,3],[4,9]]))
#Hi, I am just curious, are you guys comparing the execution time? I dont see any in your code, or I guess this is incomplete? 
