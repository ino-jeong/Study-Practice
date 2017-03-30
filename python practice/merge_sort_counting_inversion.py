# mergesort function
# A: array to be sorted
# p: start index of section to be sorted in A
# r: end index of section to be sorted in A

total_inversion = [0]

def mergeSort(A,p,r,total_inversion):

    # print("count=%d p=%d r=%d" %(c,p,r))

    if(p<r):
        q=int((p+r)/2)  #q : 1/2 point between p and r
        mergeSort(A,p,q, total_inversion) #split array recursively (1/2)
        mergeSort(A,(q+1),r, total_inversion) #split array recursively (2/2)
        # print(' p=%d,q=%d,r=%d' %(p,q,r),A)
        merge(A,p,q,r, total_inversion) #merging given partial array with sorted order
        # print(' p=%d,q=%d,r=%d' % (p, q, r), A)


# merge function for given array
def merge(A,p,q,r, total_inversion):
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
            if (q-i+1) > 0:
                total_inversion[0] += (q-i+1)
                # print('*** q-i, q, i :', q-i+1, q, i)

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


f = open('C:\\integerArray.txt', 'r')
text_data = f.readlines()

for i in range(len(text_data)):
    text_data[i] = int(text_data[i].strip('\n'))

arr = text_data
print(arr[0:9])

# arr = [8,5,6,2,4,1,0,3]
# print(arr)

last=len(arr)
mergeSort(arr,0,(last-1),total_inversion)

#check after status of arr
print(arr[0:9])
print(total_inversion)