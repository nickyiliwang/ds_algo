def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        left_idx = 0
        right_idx = 0
        merged_idx = 0

        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] < right_arr[right_idx]:
                arr[merged_idx] = left_arr[left_idx]
                left_idx += 1
            else:
                arr[merged_idx] = right_arr[right_idx]
                right_idx += 1
            merged_idx += 1

        while left_idx < len(left_arr):
            arr[merged_idx] = left_arr[left_idx]
            left_idx += 1
            merged_idx += 1

        while right_idx < len(right_arr):
            arr[merged_idx] = right_arr[right_idx]
            right_idx += 1
            merged_idx += 1

    return arr


# Explanation
def merge_sort(arr):
    # **important**: without this stopping point this will be an infinite loop
    if len(arr) > 1:
        # Split array in half
        # from the beginning to the middle point

        mid = len(arr) // 2  # round down
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # recursion to keep sorting
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        left_idx = 0
        right_idx = 0
        merged_idx = 0
        # **important**: while loop here because we want to keep comparing till one index is exhausted
        while left_idx < len(left_arr) and right_idx < len(right_arr):
            # left arr index value smaller than right
            if left_arr[left_idx] < right_arr[right_idx]:
                # save left arr index val to the larger array merged_idx
                arr[merged_idx] = left_arr[left_idx]
                left_idx += 1
            else:
                # else save right arr index val to arr index merged_idx
                arr[merged_idx] = right_arr[right_idx]
                right_idx += 1
            merged_idx += 1

        # transfer left overs
        while left_idx < len(left_arr):
            arr[merged_idx] = left_arr[left_idx]
            left_idx += 1
            merged_idx += 1

        while right_idx < len(right_arr):
            arr[merged_idx] = right_arr[right_idx]
            right_idx += 1
            merged_idx += 1

    return arr


arr_test = [2, 0, 2, 1, 1, 0]

print(merge_sort(arr_test))
