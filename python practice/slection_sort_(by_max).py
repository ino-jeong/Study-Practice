#swap function
def swap (x, y):
    temp = x
    x=y
    y=temp
    return x,y

#array to be sorted
arr = [3,0,2,1,-99,0,7,56,-89522,11,25,575,-556]

#check before status of arr
print(arr)

#selection sort by maximum
last = len(arr)
for i in range(last-1,(-1),-1):
    temp=i
    for j in range(0,i+1,1):
        if(arr[temp]<arr[j]):
            temp=j
    (arr[temp], arr[i])=swap(arr[temp],arr[i])

#check after status of arr
print(arr)

