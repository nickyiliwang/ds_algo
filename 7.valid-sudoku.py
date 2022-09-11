# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


# Example 3:
# [[".",".","4",".",".",".","6","3","."],
# [".",".",".",".",".",".",".",".","."],
# ["5",".",".",".",".",".",".","9","."],
# [".",".",".","5","6",".",".",".","."],
# ["4",".","3",".",".",".",".",".","1"],
# [".",".",".","7",".",".",".",".","."],
# [".",".",".","5",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","."]]
# Output: false

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# Trick:
# Each sub block can be split into large blocks
# To find out which sub block, we can just do (row/3 , and col/3)
# using HashDictionary (position of block) and HashSets (unique numbers)

#   0 - 9
# 0 0 1 2
# | 1
# 9 2

import collections

# neetcode


def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    # board is 9 x 9
    for r in range(9):
        for c in range(9):
            # skip empty numbers
            if board[r][c] == ".":
                # end the current loop and continues to the next loop.
                continue
            # for each number, check row, cols, and squares
            # cols and rows both cannot have the same number
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                # subBoxes/squares no repeating numbers
                    board[r][c] in squares[(r // 3, c // 3)]):
                return False

            # add each number to row and col index for next loop
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            # add each number to squares tuple for next loop
            squares[(r // 3, c // 3)].add(board[r][c])
    return True

# # my solution after reading the trick
# # subBoxValidator uses the HashDictionary with tuple of (row/3 , and col/3) + HashSet trick
# # colValidator uses {col: HashSet}
# # rowValidator uses set in each row loop in the board
# def isValidSudoku(board):
#     subBoxValidator = collections.defaultdict(set)
#     colValidator = collections.defaultdict(set)
#     # {
#     #   "0": {1, 2, 3 ...}
#     #   "1": {1, 2, 3 ...}
#     #   "...9": {1, 2, 3 ...}
#     # }
#     res = True

#     for colIdx, col in enumerate(board):
#         # we want the set to reset after each pass in row numbers
#         rowValidator = set()
#         for rowIdx, num in enumerate(col):
#             if num not in rowValidator:
#                 if num != '.':
#                     rowValidator.add(num)
#             else:
#                 res = False

#             subBoxPos = subBoxValidator[tuple([colIdx // 3, rowIdx // 3])]
#             if num not in subBoxPos:
#                 if num != '.':
#                     subBoxPos.add(num)
#             else:
#                 print('found dupe', subBoxPos, num)
#                 res = False

#             key = colValidator[rowIdx]
#             if num not in key:
#                 if num != '.':
#                     key.add(num)
#             else:
#                 res = False
#     print(subBoxValidator)
#     print(rowValidator)
#     print(res)
#     return res


board = [[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."], ["4", ".", "3", ".",
                                                                                                                                                                                                      ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."], [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]
# Output: true

isValidSudoku(board)
