# https://www.geeksforgeeks.org/adding-one-to-number-represented-as-array-of-digits/

# Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ). The digits are stored such that the most significant digit is the first element of the array.

# Examples :

# Input : [1, 2, 4]
# Output : [1, 2, 5]

# Input : [9, 9, 9]
# Output : [1, 0, 0, 0]


def AddOne(digits):
    index = len(digits) - 1

    # while the index is valid and the value at [index] == 9
    while (index >= 0 and digits[index] == 9):
        # 9 set it as 0
        digits[index] = 0
        # stepping backwards
        index -= 1

    # if index is -1 (if all digits were 9)
    if (index < 0):
        # insert an one at the beginning of the vector
        digits.insert(0, 1)

    # else increment the value at [index]
    else:
        digits[index] += 1


digits = [9, 9, 9, 9, 9]

AddOne(digits)

for digit in digits:
    print(digit, end=' ')
