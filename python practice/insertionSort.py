# array to be sorted
arr = [-89,0,5,6,6,6,6,10,9,8,7,54565,-552611,9,27,56,-54]

# check before status of arr
print(arr)

# insertion sort
last=len(arr)
for i in range(1,last):
    temp=arr[i]
    for j in range(i-1,-1,-1):
        if(temp<arr[j]):
            arr[j+1]=arr[j]
        else:
            arr[j+1]=temp
            break

# check after status of arr
print(arr)
