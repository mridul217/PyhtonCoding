def bubble_sort(arr):
    n = len(arr)

    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [7,4,5,6,9,1,2,3,7,7,5,0]
bubble_sort(arr)
print(arr)
