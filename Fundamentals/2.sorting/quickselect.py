# https://www.youtube.com/watch?v=AqMiMkPOutQ


def quickSelect(arr, l, r, k):
    def partition(arr, l, r):
        pivot = arr[r]  # last element in the arr usually
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # final swap after partition is done
        arr[i], arr[r] = arr[r], arr[i]
        return i

    pivot = partition(arr, l, r)

    if pivot == k - 1:
        return arr[pivot]

    if pivot > k - 1:
        return quickSelect(arr, l, pivot - 1, k)
    else:
        return quickSelect(arr, l, pivot + 1, k)


data = [3, 2, 3, 1, 2, 4, 5, 5, 6]
l, r = 0, len(data) - 1

print(quickSelect(data, l, r, 4))
# not sure why the answer is wrong, will check later
