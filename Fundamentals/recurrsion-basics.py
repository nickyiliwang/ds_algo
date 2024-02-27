stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sumOfEvenNums(i, lst):
    if i == len(lst):
        return 0

    value = 0
    if lst[i] % 2 == 0:
        value = lst[i]

    return sumOfEvenNums(i + 1, lst) + value


print(sumOfEvenNums(0, stuff))


def productOfEvenNums(i, lst):
    if i == len(lst):
        return None

    product = productOfEvenNums(i + 1, lst)

    if lst[i] % 2 != 0:
        return product
    if product == None:
        return lst[i]

    return lst[i] * product

print(productOfEvenNums(0, stuff))
# 3840