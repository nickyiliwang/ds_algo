def insertion(arr):
    for index in range(1, len(arr)):
        # start from total arr length
        curr = arr[index]
        # prev index
        j = index-1
        # while pre index is bigger than 0
        # and the current value is smaller than previous
        while j >= 0 and curr < arr[j]:
            # switch place with previous value
            arr[j+1] = arr[j]
            # prev index goes down by one
            j -= 1

        # end of while loop
        # prev(j) will be idx 0
        # the first element will be current value
        arr[j+1] = curr
    print(arr)


list = [9, 5, 78, 43, 73, 5, 6, 5, 32, 7, 5, 4, 3, 2, 1]

# O(n^2)
insertion(list)
