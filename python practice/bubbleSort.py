#swap function
def swap (x, y):
    temp = x
    x=y
    y=temp
    return x,y

#array to be sorted
arr = [85,0,-56,123,89122312,2,4,4,56,2,13,5,99,15,-78,-1,-0.1,27,65]

#check before status of arr
print(arr)

#bubble sort
last = len(arr)
for i in range(last-1,0,-1):
    for j in range(0,i,1):
        if (arr[j] > arr[j+1]):
            (arr[j],arr[j+1])=swap(arr[j],arr[j+1])

#check after status of arr
print(arr)
