def merge_sort(arr):
    # arr with 1 index is sorted
    if len(arr) > 1:
        # Split array in half
        # from the beginning to the middle point, double slash rounds down the division
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[(len(arr)//2):]

        # recursion to keep sorting
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left most element
        j = 0  # right most element
        k = 0  # merged array index
        while i < len(left_arr) and j < len(right_arr):
            # left arr index value smaller than right
            if left_arr[i] < right_arr[j]:
                # save left arr index val to the larger array k
                arr[k] = left_arr[i]
                # left_arr index increment
                i += 1
            else:
                # else save right arr index val to arr index k
                arr[k] = right_arr[j]
                # right_arr index increment
                j += 1
            # k index always increment
            k += 1

        # transfer left overs
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # transfer left overs
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


arr_test = [2, 3, 6, 3, 234, 26]

print(merge_sort(arr_test))
