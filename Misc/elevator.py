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


def solution(l):
    return sorted(l, key=lambda l: [int(i) for i in l.split(".")])


print(solution(["1.1.2", "1.0"]))
#  1.0,1.0.2,1.0.12,1.1.2,1.3.3
