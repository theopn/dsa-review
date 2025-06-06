def bubble_sort(arr):
    n = len(arr)
    repeat = True
    while repeat:
        repeat = False

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                repeat = True

    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i - 1

        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    return arr


def testing():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Bubble sort: ", bubble_sort(arr))
    print("Selection sort: ", selection_sort(arr))
    print("Insertion sort: ", insertion_sort(arr))


testing()
