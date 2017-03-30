
def quickSort(A,p,r):
    if(p<r and r>=0):
        #partition() : use r as a pivot, modifying array as below order. and return pivot index
        # (elements lower than pivot) - (pivot) - (elements higher than pivot)
        q=partition(A,p,r)

        #execute quickSort() recursively
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)


def partition(A,p,r):
    pivot=A[r] #use last element in A[] as pivot

    # index of last element which is lower than pivot.
    # setting this value as "first start index - 1" because this time no lower value found yet
    lastLower=p-1

    #comparing elements in A[] with pivot
    for i in range(p,r,1):
        if (A[i] <= pivot):
            lastLower=lastLower+1
            (A[lastLower], A[i])=(A[i],A[lastLower])

    lastLower = lastLower + 1
    (A[lastLower], A[r]) = (A[r], A[lastLower])
    return lastLower

# array to be sorted
arr=[4,-99,0,-99,45,3,7,6,55,1,91838,1,1,-978]

# check before status of arr
print(arr)

last=len(arr)
quickSort(arr,0,last-1)

# check after status of arr
print(arr)

