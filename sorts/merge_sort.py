def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        leftIdx = 0
        rightIdx = 0
        mergedIdx = 0
        while leftIdx < len(left_arr) and rightIdx < len(right_arr):
            if left_arr[leftIdx] < right_arr[rightIdx]:
                arr[mergedIdx] = left_arr[leftIdx]
                leftIdx += 1
            else:
                arr[mergedIdx] = right_arr[rightIdx]
                rightIdx += 1
            mergedIdx += 1

        # transfer left overs
        while leftIdx < len(left_arr):
            arr[mergedIdx] = left_arr[leftIdx]
            leftIdx += 1
            mergedIdx += 1

        while rightIdx < len(right_arr):
            arr[mergedIdx] = right_arr[rightIdx]
            rightIdx += 1
            mergedIdx += 1

    return arr


# Explanation
def merge_sort(arr):
    # arr with more than 1 length is sorted
    if len(arr) > 1:
        # Split array in half
        # from the beginning to the middle point, double slash rounds down the division

        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # recursion to keep sorting
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        leftIdx = 0
        rightIdx = 0
        mergedIdx = 0
        while leftIdx < len(left_arr) and rightIdx < len(right_arr):
            # left arr index value smaller than right
            if left_arr[leftIdx] < right_arr[rightIdx]:
                # save left arr index val to the larger array mergedIdx
                arr[mergedIdx] = left_arr[leftIdx]
                leftIdx += 1
            else:
                # else save right arr index val to arr index mergedIdx
                arr[mergedIdx] = right_arr[rightIdx]
                rightIdx += 1
            mergedIdx += 1

        # transfer left overs
        while leftIdx < len(left_arr):
            arr[mergedIdx] = left_arr[leftIdx]
            leftIdx += 1
            mergedIdx += 1

        while rightIdx < len(right_arr):
            arr[mergedIdx] = right_arr[rightIdx]
            rightIdx += 1
            mergedIdx += 1

    return arr


arr_test = [0]

print(merge_sort(arr_test))
