def countingSort(arr):
    n = len(arr)

    # Step 1 O(n): Find the maximum element and initialize count array
    k = max(arr)
    cnt = [0] * (k + 1)

    # Step 2 O(n): Find the number of occurences in each element in the array
    for i in range(n):
        cnt[arr[i]] += 1

    # Step 3 O(k): Convert count into a prefix sum array of itself
    for i in range(1, k + 1):
        cnt[i] += cnt[i - 1]

    # Step 4 O(n): Use the count array to find the index of each element
    out = [None] * n
    for i in range(n - 1, -1, -1):
        out[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] -= 1

    return out


def test():
    arr = [1, 4, 1, 2, 7, 5, 2]
    print(countingSort(arr))
    assert countingSort(arr) == [1, 1, 2, 2, 4, 5, 7]

    arr = [3, 4, 7, 11, 14, 14, 12, 20, 17, 200, 16, 20]
    print(countingSort(arr))
    assert countingSort(arr) == [3, 4, 7, 11, 12, 14, 14, 16, 17, 20, 20, 200]

    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(countingSort(arr))
    assert countingSort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("All tests passed")


test()
