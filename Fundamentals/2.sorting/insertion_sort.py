def insertion(arr):
    # start from total arr length
    for index in range(1, len(arr)):
        curr = arr[index]
        # prev index
        prevIdx = index - 1
        # while pre index is bigger or equal to 0
        # and the current value is smaller than previous
        while prevIdx >= 0 and arr[prevIdx] > curr:
            # switch place with previous value
            arr[prevIdx + 1] = arr[prevIdx]
            # prev index goes down by one
            prevIdx -= 1

        # end of while loop
        # prevIdx will be idx 0
        # the first element will be current value
        arr[prevIdx + 1] = curr
    print(arr)


list = [9, 5, 78, 43, 73, 5, 6, 5, 32, 7, 5, 4, 3, 2, 1]

# O(n^2)
insertion(list)
