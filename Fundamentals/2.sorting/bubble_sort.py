def bubble(list_a):
    # print(list_a)
    idx_len = len(list_a) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, idx_len):
            if list_a[i] < list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    print(list_a)
    return list_a


bubble([3,4])