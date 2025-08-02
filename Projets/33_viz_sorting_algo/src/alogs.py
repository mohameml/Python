
# 1. Algo Bubble sort : 
def bubble_sort_steps(numbers):
    arr = numbers[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr[:]
    yield arr


def bubble_sort(numbers) :
    arr = numbers[:]
    n = len(arr)

    for i in range(n) :
        for  j in range(0 ,n-i-1): 
            if arr[j] > arr[j + 1] : 
                arr[j]  , arr[j + 1]  = arr[j+1] , arr[j]
                yield arr[:]

    yield arr 


def selection_sort(numbers) : 
    arr = numbers[:]
    n = len(arr)
    # min_ = arr[0]
    index_min = 0 

    for i in range(n) : 
        index_min = i 
        for j in range(i + 1 , n):
            if arr[j] < arr[index_min] :
                index_min = j


        if index_min != i  :
            arr[i] , arr[index_min] = arr[index_min] , arr[i]
            yield arr[:]
            

    yield arr  


