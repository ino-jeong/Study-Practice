# mergesort function
# A: array to be sorted
# p: start index of section to be sorted in A
# r: end index of section to be sorted in A
def mergeSort(A,p,r):

    if(p<r):
        q=int((p+r)/2)  #q : 1/2 point between p and r
        
        mergeSort(A,p,q) #split array recursively (1/2)
        mergeSort(A,(q+1),r) #split array recursively (2/2)
        
        merge(A,p,q,r) #merging given partial array with sorted order
        

# merge function for given array
def merge(A,p,q,r):
    i=p
    j=q+1
    k=p
    temp=A[:] #temp=A will cause deep copy in python

    while(i<=q and j<=r):
        if(A[i]<A[j]):
            temp[k]=A[i]
            i=i+1
            k=k+1

        else:
            temp[k]=A[j]
            j=j+1
            k=k+1

    while(i<=q):
        temp[k]=A[i]
        i=i+1
        k=k+1

    while(j<=r):
        temp[k]=A[j]
        j=j+1
        k=k+1

    for i in range(p,r+1):
        A[i]=temp[i]

#array to be sorted
arr=[-78,89,11523,6,1,4,2,2,3,-895,3,3,85511,5]

#check before status of arr
print(arr)

last=len(arr) #last=6
mergeSort(arr,0,(last-1))

#check after status of arr
print(arr)
