

def bubbleSort(arr, direction=True): #direction==>default asc(true), specify 'false' for desc sort
    n = len(arr)
    swapCount = 0
    for i in range(n):
        swapDone = False
        for j in range(0, n - i - 1):
            if direction:
                if arr[j+1] < arr[j]:
                    print(arr[j], arr[j+1])
                    swapCount += 1
                    swapDone = True
                    arr[j+1], arr[j] = arr[j], arr[j+1]
            else:
                if arr[j+1] > arr[j]:
                    print(arr[j], arr[j+1])
                    swapCount += 1
                    swapDone = True
                    arr[j+1], arr[j] = arr[j], arr[j+1]

        if not swapDone:
            return swapCount
    return swapCount

def selectionSort(arr, direction=True):
    for i in range(len(arr)):
        minIndex = i
        if direction:
            for j in range(i+1, len(arr)):
                if(arr[minIndex] > arr[j]):
                    minIndex = j
        else:
            for j in range(i+1, len(arr)):
                if(arr[minIndex] < arr[j]):
                    minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def insertionSort(arr, direction=True):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        if direction:
            while j >= 0 and temp < arr[j]:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = temp
        else:
            while j >= 0 and temp > arr[j]:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = temp

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]

    insertPoint = low -1
    for j in range(low, high):
        if arr[j] < pivot:
            insertPoint +=1
            arr[insertPoint], arr[j] = arr[j], arr[insertPoint]

    arr[insertPoint +1], arr[high] = arr[high], arr[insertPoint +1]

    return insertPoint+1




# def quickSort(arr, low, high, direction=True):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)
#
# def partition(arr, low, high, direction=True):
#     pivot = arr[high]
#
#     insertPoint = low -1
#     for j in range(low, high):
#         if direction:
#             if arr[j] < pivot:
#                 insertPoint +=1
#                 arr[insertPoint], arr[j] = arr[j], arr[insertPoint]
#             else:
#                 if arr[j] > pivot:
#                     insertPoint += 1
#                     arr[insertPoint], arr[j] = arr[j], arr[insertPoint]
#
#     arr[insertPoint +1], arr[high] = arr[high], arr[insertPoint +1]
#
#     return insertPoint+1