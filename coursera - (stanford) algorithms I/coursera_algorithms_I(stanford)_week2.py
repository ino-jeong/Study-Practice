def quick_sort(arr, start, end, comp_cnt):
    if (end - start + 1) <= 1:
        return

    # pivot_idx = start
    # pivot_idx = end

    middle = int((end - start) / 2) + start
    if arr[start] < arr[middle]:
        if arr[middle] <= arr[end]:
            median = middle
        elif arr[start] < arr[end]:
            median = end
        else:
            median = start
    else:
        if arr[start] <= arr[end]:
            median = start
        elif arr[middle] < arr[end]:
            median = end
        else:
            median = middle
    pivot_idx = median

    arr[start], arr[pivot_idx] = arr[pivot_idx], arr[start]

    i = start+1 # last index of element which are smaller than pivot
    for j in range(start + 1 , end + 1):
       if arr[j] < arr[start]:
           arr[i], arr[j] = arr[j], arr[i]
           i += 1

    arr[start], arr[i-1] = arr[i-1], arr[start]

    if (i-2-start)>0:
        comp_cnt[0] = comp_cnt[0] + (i - 2 - start)
    if (end-i)>0:
        comp_cnt[0] = comp_cnt[0] + (end - i)

    # comp_cnt[0] = comp_cnt[0] + (i-2-start) + (end-i)
    quick_sort(arr, start, i-2, comp_cnt)
    quick_sort(arr, i, end, comp_cnt)

f=open('C:\QuickSort.txt','r')
test_arr = f.readlines()

for i in range(len(test_arr)):
    test_arr[i] = int(test_arr[i].strip('\n'))
print(test_arr[0:14])

comp_cnt = [0]

last_idx = len(test_arr) - 1
quick_sort(test_arr, 0, last_idx, comp_cnt)

print(test_arr[0:14])
print(comp_cnt[0]+len(test_arr)-1)



