def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)

    # arrssign elements to each array
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + j + 1]

    L[n1], R[n2] = float("inf"), float("inf")
    i, j = 0, 0

    for k in range(l, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

    return arr


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr


def quick_sort(arr, l, r):
    if l < r:
        m = partition(arr, l, r)
        quick_sort(arr, l, m - 1)
        quick_sort(arr, m + 1, r)
    return arr


def partition(arr, l, r):
    p = arr[r]  # rightmost element as the pivot
    i = l - 1
    for j in range(l, r + 1):
        if arr[j] < p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


# Merge sort testing
arr = [3, 4, 7, 11, 14.0, 14, 12, 20, 17, 200, 16, 20]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n")
merge_sort(arr, 0, n - 1)
print("\nSorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")

print()

# quick sort testinv
arr = [3, 4, 7, 11, 14.0, 14, 12, 20, 17, 200, 16, 20]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\n")
quick_sort(arr, 0, n - 1)
print("\nSorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
